import time

from playwright.sync_api import Page, expect ,Playwright


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://rahulshettyacademy.com")

def test_playwrightShortCut(page:Page):
    #page fixtures supports only chrome and ms-edge browser engine headless mode
    page.goto("https://rahulshettyacademy.com")

def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link",name="terms and conditions").click()
    page.get_by_role("button",name="Sign In").click()
    expect(page.get_by_text("incorrect username/password")).to_be_visible()


# lable should have lable tag
# object & label should be associated with each other

#CSSSelector
#synax  #id   .classname   tagname


def test_firefoxBrowser(playwright: Playwright):
    firefox_browser = playwright.firefox
    browser = firefox_browser.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    # expect(page.get_by_text("incorrect username/password")).to_be_visible()
    time.sleep(10)

