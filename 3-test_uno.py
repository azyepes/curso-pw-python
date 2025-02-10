import re
from playwright.sync_api import sync_playwright, Page, expect, Playwright

def test_uno(page: Page):
    page.goto("https://playwright.dev/")
    # expect(page).to_have_title("Playwright")
    expect(page).to_have_title(re.compile(r"Fast"))
    
    button_uno = page.locator("text=Get started")
    expect(button_uno).to_have_attribute("href", "/docs/intro")
    button_uno.click()
    
    
    page.screenshot(path="imagenes/getstartedexample.png")
    
    # Validar que la URL sea la correcta
    expect(page).to_have_url(re.compile(r".*/docs/intro"))