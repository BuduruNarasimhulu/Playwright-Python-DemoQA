import re
from playwright.sync_api import Playwright, sync_playwright, expect

file = r"C:\Users\al20271\Pictures\Screenshots\Screenshot 2024-08-23 174612.png"

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=2000)
    context = browser.new_context(record_video_dir="videos/")
    page = context.new_page()
    page.goto("https://demoqa.com/")
    page.locator("svg").first.click()
    #Textbox
    page.get_by_text("Text Box").click()
    page.get_by_placeholder("Full Name").click()
    page.get_by_placeholder("Full Name").fill("Narasimhulu Buduru")
    page.get_by_placeholder("name@example.com").click()
    page.get_by_placeholder("name@example.com").fill("narasimhulubuduru4822@gmail.com")
    page.get_by_placeholder("Current Address").click()
    page.get_by_placeholder("Current Address").fill("bengaluru")
    page.locator("#permanentAddress").click()
    page.locator("#permanentAddress").fill("naidupeta")
    page.get_by_role("button", name="Submit").click()
    #checkbox
    page.get_by_text("Check Box").click()
    page.locator("#tree-node").get_by_role("img").nth(3).click()
    #Radio button
    page.get_by_text("Radio Button").click()
    page.get_by_text("Yes").click()
    #Web Table
    page.get_by_text("Web Tables").click()
    page.get_by_role("button", name="Add").click()
    page.get_by_placeholder("First Name").click()
    page.get_by_placeholder("First Name").fill("Narasimhulu")
    page.get_by_placeholder("Last Name").click()
    page.get_by_placeholder("Last Name").fill("Buduru")
    page.get_by_placeholder("name@example.com").click()
    page.get_by_placeholder("name@example.com").fill("narasimhulubuduru4822@gmail.com")
    page.get_by_placeholder("Age").click()
    page.get_by_placeholder("Age").fill("23")
    page.get_by_placeholder("Salary").click()
    page.get_by_placeholder("Salary").fill("00000")
    page.get_by_placeholder("Department").click()
    page.get_by_placeholder("Department").fill("qa")
    #buttons
    page.get_by_role("button", name="Submit").click()
    page.get_by_text("Buttons").click()
    page.get_by_role("button", name="Right Click Me").click(button="right")
    page.get_by_role("button", name="Double Click Me").dblclick()
    #Forms
    page.get_by_text("Forms").click()
    page.get_by_text("Practice Form").click()
    page.get_by_placeholder("First Name").click()
    page.get_by_placeholder("First Name").fill("Narasimhulu")
    page.get_by_placeholder("Last Name").click()
    page.get_by_placeholder("Last Name").fill("Buduru")
    page.get_by_placeholder("name@example.com").click()
    page.get_by_placeholder("name@example.com").fill("narasimhulubuduru4822@gmail.com")
    page.get_by_text("Male", exact=True).click()
    page.get_by_placeholder("Mobile Number").click()
    page.get_by_placeholder("Mobile Number").fill("6303759197")
    page.locator("#dateOfBirthInput").click()
    page.get_by_role("combobox").nth(1).select_option("2001")
    page.locator("div").filter(has_text=re.compile(
        r"^JanuaryFebruaryMarchAprilMayJuneJulyAugustSeptemberOctoberNovemberDecember$")).get_by_role(
        "combobox").select_option("6")
    page.get_by_label("Choose Wednesday, July 25th,").click()
    page.locator(".subjects-auto-complete__value-container").click()
    page.locator("#subjectsInput").fill("Playwright")
    page.get_by_text("Sports").click()
    upload_input = page.locator("input[type=file]#uploadPicture")
    upload_input.wait_for(state="visible", timeout=60000)
    upload_input.set_input_files(file)

    page.get_by_placeholder("Current Address").click()
    page.get_by_placeholder("Current Address").fill("India")
    page.locator(".css-tlfecz-indicatorContainer").first.click()
    page.get_by_text("NCR", exact=True).click()
    page.locator("div").filter(has_text=re.compile(r"^Select City$")).nth(3).click()
    page.get_by_text("Delhi", exact=True).click()
    page.get_by_role("button", name="Submit").click()
    page.go_back()
    #alerts
    page.get_by_text("Alerts, Frame & Windows").click()
    page.get_by_text("Alerts", exact=True).click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.locator("#alertButton").click()
    #dialog boxs
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.locator("#timerAlertButton").click()
    page.locator("li").filter(has_text="Modal Dialogs").click()
    page.get_by_role("button", name="Small modal").click()
    page.locator("#closeSmallModal").click()
    page.get_by_role("button", name="Large modal").click()
    page.locator("#closeLargeModal").click()

    #registration and login page
    page.get_by_text("Book Store Application").click()
    page.get_by_text("Login").click()
    page.get_by_role("button", name="New User").click()
    page.get_by_placeholder("First Name").click()
    page.get_by_placeholder("First Name").fill("Narasimhulu")
    page.get_by_placeholder("Last Name").click()
    page.get_by_placeholder("Last Name").fill("Buduru")
    page.get_by_placeholder("UserName").click()
    page.get_by_placeholder("UserName").fill("narasimhulubuduru4822@gmail.com")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("Narasimhulu@12")
    captcha_frame = page.locator("iframe[name='a-p41wmc7szk7r']").content_frame

    page.get_by_role("button", name="Register").click()
    page.get_by_role("button", name="Back to Login").click()
    page.get_by_placeholder("UserName").click()
    page.get_by_placeholder("UserName").fill("narasimhulubuduru4822@gmail.com")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("Narasimhulu@12")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Log out").click()
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
