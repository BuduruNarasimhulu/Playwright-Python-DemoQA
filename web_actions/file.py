import re
from playwright.sync_api import Playwright, sync_playwright, expect

file = r"C:\Users\al20271\Pictures\Screenshots\Screenshot 2024-08-23 174612.png"

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/")
    page.locator("path").first.click()
    page.get_by_text("Forms").click()
    page.get_by_text("Practice Form").click()
    page.get_by_placeholder("First Name").click()
    page.get_by_placeholder("First Name").fill("narasimhulu")
    page.get_by_placeholder("Last Name").click()
    page.get_by_placeholder("Last Name").fill("buduru")
    page.get_by_placeholder("name@example.com").click()
    page.get_by_placeholder("name@example.com").fill("narasimhulubuduru4822@gmail.com")
    page.get_by_text("Male", exact=True).click()
    page.get_by_text("Female").click()
    page.get_by_text("Other").click()
    page.get_by_placeholder("Mobile Number").click()
    page.get_by_placeholder("Mobile Number").fill("6303759197")
    page.locator("#dateOfBirthInput").click()
    page.get_by_role("combobox").nth(1).select_option("2001")
    page.locator("div").filter(has_text=re.compile(r"^JanuaryFebruaryMarchAprilMayJuneJulyAugustSeptemberOctoberNovemberDecember$")).get_by_role("combobox").select_option("6")  # Closing parenthesis added here
    page.get_by_label("Choose Wednesday, July 25th,").click()
    page.locator(".subjects-auto-complete__value-container").click()
    page.locator("#subjectsInput").fill("Playwright")
    page.get_by_text("Sports").click()
    page.get_by_text("Reading").click()
    page.get_by_text("Music").click()
    page.locator(".subjects-auto-complete__value-container").click()
    page.locator("#subjectsInput").fill("playwright")

    # Wait for the file input to be visible and enabled
    upload_input = page.locator("input[type=file]#uploadPicture")
    upload_input.wait_for(state="visible", timeout=60000)
    upload_input.set_input_files(file)

    page.get_by_placeholder("Current Address").click()
    page.get_by_placeholder("Current Address").fill("naidupeta")
    page.locator("div").filter(has_text=re.compile(r"^Select State$")).nth(3).click()
    page.get_by_text("NCR", exact=True).click()
    page.get_by_text("Select City").click()
    page.get_by_text("Delhi", exact=True).click()
    page.get_by_role("button", name="Submit").click()
    page.goto("https://demoqa.com/elements")

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
