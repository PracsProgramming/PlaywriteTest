from playwright.sync_api import Page, expect


def test_UIValidationDynamicScript(page: Page):
    # two items added in cart : iphonex and nokia edge
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()

    iphone_X = page.locator("app-card").filter(has_text="iphone X")
    iphone_X.get_by_role("button").click()
    Nokia_Edge = page.locator("app-card").filter(has_text="Nokia Edge")
    Nokia_Edge.get_by_role("button").click()

    page.get_by_text("Checkout").click()

    expect(page.locator(".media-body")).to_have_count(2)


def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as newPageInfo:
        page.locator(".blinkingText").click()
        child_page = newPageInfo.value
        text = child_page.locator(".red").text_content()
        print(text)
        words = text.split("at")
        email = words[1].strip().split(" ")[0]
        assert  email == "mentor@rahulshettyacademy.com"













