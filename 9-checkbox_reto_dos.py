import re
import time

from playwright.sync_api import Page, expect, sync_playwright, Playwright
  
# pytest 9-checkbox_reto_dos.py

def test_checkbox_reto_dos(playwright: Playwright) -> None:
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
    
    page.goto("https://datatables.net/extensions/select/examples/checkbox/checkbox.html")
    page.set_default_timeout(5000)
    expect(page).to_have_title("DataTables example - No ordering")
    
    # Scroll down
    page.mouse.wheel(0, 400) # Cordenadas en x, y x=0 y=400
    time.sleep(0.5)
    
    # Check los 3 primero y pasa a la siguiente pagina, check 3 más y pasa a la siguiente pagina
    # for i in range(1,11): # (1,11,2) 1-> donde empieza 11-> donde termina -1 y 2-> saltos
    #     page.locator(f"(//input[@aria-label='Select row'])[{i}]").click()
    #     if i == 3:
    #         page.locator("//button[normalize-space()='2']").click()
    #     elif i == 6:
    #         page.locator("//button[normalize-space()='3']").click()
    
    # Check los 11 y pasa a la siguiente pagina, check 11 más y pasa a la siguiente pagina, etc.
    
    count_pages = page.locator("//*[@data-dt-idx >= 0]").count()
    
    for i in range(1,count_pages+1):
        if i == 1:
            pass
        else:
            page.locator(f"//button[normalize-space()='{i}']").click()
        count_entries = page.locator("//table[@id='example']/tbody/tr").count()
        for j in range(1,count_entries+1):
            page.locator(f"(//input[@aria-label='Select row'])[{j}]").click()
      

   # ------
    context.close()
    browser.close()