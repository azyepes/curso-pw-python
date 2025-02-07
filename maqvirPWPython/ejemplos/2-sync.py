import asyncio
from logging import handlers
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=3000)
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    page.screenshot(path="imagenes/sync_example.png")
    print (page.title())
    browser.close()