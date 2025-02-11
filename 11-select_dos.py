import re
from playwright.sync_api import Page, expect, sync_playwright, Playwright
from BasePage import BasePage

t = 3
path = "Imagenes/Select"

def test_select_dos(playwright: Playwright) -> None:
    
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
    F.Goto("https://validaciones.rodrigovillanueva.com.mx/ComboBox_ok.html", "Formulario de Ejemplo")
    
    # Select function
    F.Select("#comboBox1", "Valor 2", t)
    F.Select("#comboBox2", "5", t)
    F.Select("#os", "linux", t)
    F.Select("#version", "Ubuntu")
    
    F.Click("//button[normalize-space()='Enviar']")
    F.Validate_text("//div[@id='flashMessage']", "Formulario enviado exitosamente")


    # ---------------------
    context.close()
    browser.close()