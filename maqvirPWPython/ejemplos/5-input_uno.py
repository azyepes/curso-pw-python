import re
import time

from playwright.sync_api import Page, expect, sync_playwright, Playwright

# pytest --slowmo 500 --headed 5-input_uno.py

# def test_input_uno(page: Page):
def test_input_uno(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=200)
    # context = browser.new_context()
    context = browser.new_context(
        # viewport={"width": 1920, "height": 1080},
        record_video_dir="videos/input_uno",
    )
    page = context.new_page() 
    page.set_viewport_size({"width": 1600, "height": 800})
    
    page.goto("https://rodrigovillanueva.com.mx/")
    expect(page).to_have_title("Home Page | RodrigoVillanueva.com.mx")
    page.locator("//span[normalize-space()='Prácticas2']").click()
    
    # Tiempo de espera
    page.set_default_timeout(5000)
    
    # Enabled
    nombre = page.locator("//input[@id='nombre']")
    expect(nombre).to_be_enabled()
    
    # Validaciones o Assert
    apellidos = page.locator("//input[@id='apellidos']")
    expect(apellidos).to_be_visible()
    
    # Empty - Que el campo esté vacío
    tel = page.locator("//input[@id='tel']")
    expect(tel).to_be_empty()
    
    # Que contenga el ID
    email = page.locator("//input[@id='email']")
    expect(email).to_have_id("email")
    
    page.locator("//input[@id='nombre']").fill("John")
    page.locator("//input[@id='apellidos']").fill("Doe")
    page.locator("//input[@id='tel']").fill("3050085414")
    
    # Tiempo forzado
    time.sleep(1)
    
    page.locator("//input[@id='email']").fill("johndoe@me.com")
    page.locator("//input[@id='direccion']").fill("123 Main Street")
    
    
    # Que sea visible
    # enviarButton = page.locator("//button[normalize-space()='Enviar']")
    # expect(enviarButton).to_be_visible()
    
    # if enviarButton.is_visible():
    if page.is_visible("//button[normalize-space()='Enviar']"):
        # enviarButton.click()
        page.locator("//button[normalize-space()='Enviar']").click()
    else:
        page.locator("//button[normalize-space()='Limpiar']").click()
        print("No se encuentra el boton")
    
    # page.locator("//button[normalize-space()='Enviar']").click()
    expect(page.locator("//div[@id='flashMessage']")).to_contain_text(re.compile(r"El formulario se ha enviado correctamente."))
    
    context.close()
    