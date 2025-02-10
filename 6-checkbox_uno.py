import re
import time

from playwright.sync_api import Page, expect, sync_playwright, Playwright

# pytest --slowmo 500 --headed 6-checkbox.py
# pytest 6-checkbox.py

def test_checkbox_uno(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=200)
    context = browser.new_context(
        viewport={"width": 1600, "height": 1020},
        # record_video_dir="videos/checkbox",
    )
    page = context.new_page() 
    # page.set_viewport_size({"width": 1600, "height": 800})
    
    page.goto("https://demoqa.com/")
    page.set_default_timeout(5000)
    expect(page).to_have_title("DEMOQA")
    
    page.locator("text=Elements").click()
    page.locator("text=Check Box").click()
    
    home_list = page.get_by_label("Toggle")  #.locator("//button[@title='Toggle']//*[name()='svg']") 
    home_checkbox = page.locator("//span[@class='rct-checkbox']//*[name()='svg']")
    
    expect(home_list).to_be_visible()
    expect(home_list).to_be_enabled()
    
    expect(home_checkbox).to_be_visible()
    expect(home_checkbox).to_be_enabled()
    
    desktop_list = page.get_by_label("Toggle").nth(1)  #.locator("(//*[name()='svg'][@class='rct-icon rct-icon-expand-close'])[1]")
    desktop_checkbox = page.locator("(//*[name()='svg'][@class='rct-icon rct-icon-uncheck'])[2]")
    
    commands_checkbox = page.get_by_text("commands")  #.locator("(//*[name()='svg'][@class='rct-icon rct-icon-uncheck'])[4]")
    
    home_list.click()
    desktop_list.click()
    commands_checkbox.click()
    
    expect(page.locator("//span[normalize-space()='You have selected :']")).to_contain_text(re.compile(r"You have selected :"))
    expect(page.locator("//span[@class='text-success']")).to_contain_text(re.compile(r"commands"))
    
    
    
    # Cerrar context y el navegador
    context.close()
    browser.close()