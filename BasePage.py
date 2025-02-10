import re
import time

from playwright.sync_api import Page, expect, sync_playwright, Playwright


class BasePage:
    
    # Constructor
    def __init__(self, page): 
        self.page = page
        
    def Default_Timeout(self, t=5000): #z_time = 5000 default time en caso no se pase
        self.page.set_default_timeout(t)
        
    def Timeout(self, t=0.5):
        time.sleep(t)
        
    def Scroll_Down_Up(self, x_position, y_position, t=0.5):
        self.page.mouse.wheel(x_position, y_position)
        time.sleep(t)
        
    def Click(self, locator, t=0.5):
        selector = self.page.locator(locator)
        selector.click()
        time.sleep(t)
        
    def Fill_text(self, locator, text):
        selector = self.page.locator(locator)
        try:
        # expect(selector).to_be_visible()
        # expect(selector).to_be_enabled()
        # expect(selector).to_be_empty()
            # print("All Good")
            assert selector.is_visible() == True
        # assert selector.is_enabled() == enabled
        # assert selector.is_empty() == empty
            selector.fill(text)
        except Exception as e:
            print(f"Error: {e}")
            
        time.sleep(1)