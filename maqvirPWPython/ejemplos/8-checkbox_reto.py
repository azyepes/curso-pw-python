import re
import time
from playwright.sync_api import Page, expect, sync_playwright, Playwright

# pytest 8-checkbox_reto.py

def test_checkbox_reto(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(
        headless=False, 
        slow_mo=500
    )
    
    context = browser.new_context(
        viewport={"width": 1600, "height": 1020},
        # record_video_dir="videos/checkbox",
    )
    
    page = context.new_page() 
    # page.set_viewport_size({"width": 1600, "height": 800})
    
    page.goto("https://demoqa.com/automation-practice-form")
    page.set_default_timeout(5000)
    expect(page).to_have_title("DEMOQA")
    
    # Scroll down
    page.mouse.wheel(0, 400) # Cordenadas en x, y x=0 y=400
    time.sleep(1)
    
    page.get_by_placeholder("First Name").fill("John")
    page.get_by_placeholder("Last Name").fill("Doe")
    page.get_by_placeholder("name@example.com").fill("johndoe@me.com")
    
    page.locator("//label[normalize-space()='Male']").click()
    # page.get_by_text("Male").click()
    
    
    page.get_by_placeholder("Mobile Number").fill("305005414")
    
    # page.locator("//label[normalize-space()='Sports']").click()
    # page.locator("//label[normalize-space()='Reading']").check()
    # page.locator("//label[normalize-space()='Reading']").uncheck()
    # assert page.locator("//label[normalize-space()='Reading']").is_checked() == True
    # assert page.locator("//label[normalize-space()='Music']").is_checked() == False
    
    
    # Ciclo for para hace check a varios checkbox
    for i in range(1,4):
        page.locator(f"label[for='hobbies-checkbox-{i}']").check()
    
    
    address = page.get_by_placeholder("Current Address")
    address.fill("123 Main Street")
    expect(address).to_be_visible()
    
    # page.get_by_role("button", name="Submit").click()
    # expect(page.locator("//p[@id='name']")).to_contain_text(re.compile(r"Name:John Doe"))
    
    
    context.close()
    browser.close()