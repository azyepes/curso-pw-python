import re
import time

from playwright.sync_api import Page, expect, sync_playwright, Playwright
from BasePage import BasePage

# Variable global
t = 3
path = "Imagenes/Selector"

def test_select_uno(playwright: Playwright) -> None:
    
    browser = playwright.chromium.launch(
        headless=False, 
        slow_mo=t*100
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
    F.Default_Timeout(t*1000) # page.set_default_timeout(5000)

    # Expected title
    expect(page).to_have_title("DEMOQA")
    
    # Go to practice form
    F.Click("(//div[@class='card mt-4 top-card'])[2]") # Click en Forms
    F.Click("//span[normalize-space()='Practice Form']") # Click en practice forms
        
    # Sroll down
    F.Scroll_Down_Up(0, 400, t) # page.mouse.wheel(0, 200) # Cordenadas en x, y x=0 y=400
    
    # Función de espera
    # F.Timeout(t) # time.sleep(1)
    
    # Función fill text, click
    F.Fill_text("//input[@id='firstName']", "John") # Fill first name
    F.Fill_text("//input[@id='lastName']", "Doe") # Fill last name
    F.Fill_text("//input[@id='userEmail']", "johndoe@me.com") # Fill email
    F.Screenshot(path + "/email.png")
    
    
    
    F.Click("//label[normalize-space()='Male']") # Click Male
    
    F.Fill_text("//input[@id='userNumber']", "3050085414") # Fill phone number
    F.Fill_text("//textarea[@id='currentAddress']", "123 Main Street") # Fill address
    
    F.Click("//div[text()='Select State']")
    F.Click("//div[text()='NCR']")
    
    F.Click("//div[text()='Select City']")
    F.Click("//div[text()='Delhi']")
    # Click submit
    # F.Click("//button[@id='submit']") # page.locator("//button[@id='submit']").click()
    
    # time.sleep(5)

    
    # ----
    
    context.close()
    browser.close()