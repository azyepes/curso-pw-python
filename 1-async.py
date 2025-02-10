import asyncio
from logging import handlers
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=1000)
        page = await browser.new_page()
        await page.goto("https://playwright.dev/")
        await page.screenshot(path="imagenes/async_example.png")
        print (await page.title())
        await browser.close()
        
asyncio.run(main())