from playwright.sync_api import Page, Route

fakepayloadresponse = {"data":[],"message":"No Orders"}


def intercept_response(route:Route):
    route.fulfill(json=fakepayloadresponse)


def test_network_1(page: Page):
    # login
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="login").click()

    page.get_by_role("button", name="ORDERS").click()

    order_text = page.locator(".mt-4").text_content()
    print(order_text)
