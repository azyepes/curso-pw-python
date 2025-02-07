import re
from playwright.sync_api import Page, expect

# pytest --slowmo 2000 --headed 4-test_dos.py

def test_dos(page: Page):
    page.goto("https://demoqa.com/")
    expect(page).to_have_title("DEMOQA")
    
    page.locator("text=Elements").click()
    page.screenshot(path="imagenes/elements.png")
    expect(page).to_have_url(re.compile(r".*/elements"))
    
    page.locator("text=Text Box").click()
    expect(page).to_have_url(re.compile(r".*/text-box"))
    
    page.locator("//input[@id='userName']").fill("John Doe")
    page.locator("#userEmail").fill("johndoe@me.com")
    page.locator("#currentAddress").fill("123 Main Street")
    page.locator("#permanentAddress").fill("123 Main Street")
    
    page.locator("#submit").click()
    expect(page.locator("//p[@id='name']")).to_contain_text(re.compile(r"Name:John Doe"))
    page.screenshot(path="imagenes/text_box_filled.png")
    
    