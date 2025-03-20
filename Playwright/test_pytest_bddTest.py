import pytest

from pytest_bdd import given, when, then, scenarios, parsers

from POM_Pattern.LoginPage import LoginPageClass
from conftest import browserInstance
from utils.apibaseFramework import APIUtilsFramework

scenarios("features/orderTransaction.feature")


@pytest.fixture
def shared_data():
    return {}


@given(parsers.parse('place the item in order with {username} and {password}'))
def place_item_order(playwright, username, password,shared_data):
    user_credentials = {}
    user_credentials["userEmail"] = username
    user_credentials["userPassword"] = password
    api_utils = APIUtilsFramework()
    OrderId = api_utils.createOrder(playwright, user_credentials)
    shared_data['orderId'] = OrderId


@given('the user is on landing page')
def goto_landing_page(browserInstance,shared_data):
    loginPage = LoginPageClass(browserInstance)
    loginPage.navigate()
    shared_data['login_page'] = loginPage


@when(parsers.parse('I login to portal with {username} and {password}'))
def login_to_portal(username, password, shared_data):
    loginPage = shared_data['login_page']
    DashboardPage = loginPage.login(username, password)
    shared_data['Dashboard'] = DashboardPage


@when('navigate to orders page')
def navigate_to_orders(shared_data):
    DashboardPage = shared_data['Dashboard']
    OrdersHistoryPage = DashboardPage.selectOrdersNavLink()
    shared_data['OrderHistory'] = OrdersHistoryPage


@when('select order Id')
def select_order_id(shared_data):
    OrdersHistoryPage = shared_data['OrderHistory']
    OrderId = shared_data['orderId']
    orderDetailsPage = OrdersHistoryPage.selectOrder(OrderId)
    shared_data['OrderDetails'] = orderDetailsPage


@then('order message is successfully displayed')
def verify_order_message(shared_data):
    orderDetailsPage = shared_data['OrderDetails']
    orderDetailsPage.verifyOrderMessage()
