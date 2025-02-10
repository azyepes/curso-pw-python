import re
import time

from playwright.sync_api import Page, expect, sync_playwright, Playwright
from BasePage import BasePage

def test_select_uno(playwright: Playwright) -> None:
    
    browser = playwright.chromium.launch(
        headless=False, 
        slow_mo=300
    )
    
    context = browser.new_context(
        viewport={"width": 1600, "height": 1020},
        # record_video_dir="videos/checkbox", 
    )
    
    page = context.new_page() 
    # page.set_viewport_size({"width": 1600, "height": 800})
    
    # Creando Objeto de funciones globales
    F = BasePage(page)
    
    # Go to https://demoqa.com
    page.goto("https://demoqa.com")
    
    # Default timeout para esperar en la pagina
    F.Default_Timeout(5000) # page.set_default_timeout(5000)

    # Expected title
    expect(page).to_have_title("DEMOQA")
    
    # Go to practice form
    F.Click("(//div[@class='card mt-4 top-card'])[2]") # page.get_by_text("Forms").click()
    F.Click("//span[normalize-space()='Practice Form']") # page.get_by_text("Practice Form").click()
        
    # Sroll down
    F.Scroll_Down_Up(0, 400, 1) # page.mouse.wheel(0, 200) # Cordenadas en x, y x=0 y=400
    
    # Función de espera
    # F.Timeout(1) # time.sleep(1)
    
    # Función fill text, click
    F.Fill_text("//input[@id='firstName']", "John") # page.locator("//input[@id='firstName']").fill("John")}
    F.Fill_text("//input[@id='lastName']", "Doe") # page.locator("//input[@id='lastName']").fill("Doe")
    F.Fill_text("//input[@id='userEmail']", "johndoe@me.com") # page.locator("//input[@id='userEmail']").fill("johndoe@me.com")
    
    F.Click("//label[normalize-space()='Male']") # page.get_by_text("Male").click()
    
    F.Fill_text("//input[@id='userNumber']", "3050085414") # page.locator("//input[@id='userNumber']").fill("1234567890")
    F.Fill_text("//textarea[@id='currentAddress']", "123 Main Street") # page.locator("//textarea[@id='currentAddress']").fill("123 Main Street")
    
    # Click submit
    # F.Click("//button[@id='submit']") # page.locator("//button[@id='submit']").click()
    
    # time.sleep(5)

    
    # ----
    
    context.close()
    browser.close()