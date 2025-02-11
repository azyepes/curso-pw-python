import re
import time

from playwright.sync_api import Page, expect, sync_playwright, Playwright


class BasePage:
    
    # Constructor
    def __init__(self, page): 
        self.page = page
        
    def Goto(self, url, title):
        self.page.goto(url)
        expect(self.page).to_have_title(re.compile(rf"{title}"))
        
    def Default_Timeout(self, t=5000): #z_time = 5000 default time en caso no se pase
        self.page.set_default_timeout(t)
        
    def Timeout(self, t=0.5):
        time.sleep(t)
        
    def Scroll_Down_Up(self, x_position, y_position, t=0.5):
        self.page.mouse.wheel(x_position, y_position)
        time.sleep(t)
        
    def Click(self, locator, t=0.5):
        selector = self.page.locator(locator)
        
        expect(selector).to_be_visible()
        expect(selector).to_be_enabled()
        
        selector.click()
        time.sleep(t)
        
    def Fill_text(self, locator, text):
        selector = self.page.locator(locator)
        # try:
        expect(selector).to_be_visible()
        expect(selector).to_be_enabled()
        expect(selector).to_be_empty()
        
        selector.highlight()
        selector.fill(text)
        # except Exception as e:
            # print(f"Error: {e}")
            
        time.sleep(1)
        
    def Screenshot(self, path, t=0.5):
        self.page.screenshot(path=path)
        time.sleep(t)
    
    def Select(self, locator, value, t=0.5):
        selector = self.page.locator(locator)
        
        expect(selector).to_be_visible()
        expect(selector).to_be_enabled()
        
        selector.select_option(value)
        time.sleep(t)
        
    def Validate_text(self, locator, text, t=0.5):
        selector = self.page.locator(locator)
        expect(selector).to_contain_text(re.compile(rf"{text}"))
        time.sleep(t)