import json

import pytest
from playwright.sync_api import Playwright

from POM_Pattern.LoginPage import  LoginPageClass
from utils.apibaseFramework import APIUtilsFramework

#json file  -> util ->access into test.
with open("Data/credentials.json") as f:
    test_data = json.load(f)
    # print(test_data)
    user_credentials_list = test_data["user_credentials"]
    # print(user_credentials)

@pytest.mark.parametrize('user_credentials',user_credentials_list)
def test_e2e_web_api(playwright: Playwright,browserInstance,user_credentials):
    user_Email = user_credentials["userEmail"]
    user_Password = user_credentials["userPassword"]
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()

    # create order
    api_utils = APIUtilsFramework()
    OrderId = api_utils.createOrder(playwright,user_credentials)

    #login
    loginPage = LoginPageClass(browserInstance)
    loginPage.navigate()
     #dashboard page
    DashboardPage = loginPage.login(user_Email, user_Password)
    #order history
    OrdersHistoryPage = DashboardPage.selectOrdersNavLink()

    # order Details page
    orderDetailsPage = OrdersHistoryPage.selectOrder(OrderId)
    orderDetailsPage.verifyOrderMessage()


