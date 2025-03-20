import time

import pytest
from playwright.sync_api import Page, Route, Playwright, expect


from utils.apibase import APIUtils

fakepayloadresponse = {"data":[],"message":"No Orders"}


def intercept_request(route:Route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=67dab02cc019fb1ad62e6c2a")

@pytest.mark.smoke
def test_network_2(page: Page):
    # login
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="login").click()

    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button",name="View").first.click()
    time.sleep(3)
    message = page.locator(".blink_me").text_content()
    print(message)


def test_session_storage(playwright:Playwright):
    api_utils =  APIUtils()
    get_token = api_utils.get_token(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.add_init_script(f"""localStorage.setItem('token','{get_token}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button",name= "ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()