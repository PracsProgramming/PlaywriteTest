# from tkinter import dialog
import time

from playwright.sync_api import Page, expect



def test_UIChecks(page : Page):

    # Hide/Display & PlaceHolder

    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button",name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    time.sleep(2)
    #Alert
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button",name="Confirm").click()
    time.sleep(2)
    #Mouse Hover
    page.locator("#mousehover").hover()
    page.get_by_role("link",name="Top").click()
    time.sleep(2)
    #
    # #Frames
    #id
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link",name="All Access plan").click()
    time.sleep(2)
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")
    time.sleep(2)


def test_webTable(page:Page):
    global colValuePrice
    # #WebTable
    # #Identify price colomn ,rice coloum ,extract price
    #
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    time.sleep(2)
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() >0:
            colValuePrice = index
            print(f"Price coloumn value is {colValuePrice}")
            break
    #
    riceRow =  page.locator("tr").filter(has_text="rice")
    expect(riceRow.locator("td").nth(colValuePrice)).to_have_text("37")
    time.sleep(2)
