from playwright.async_api import async_playwright
import asyncio
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://orion-med.ru/")
        await page.screenshot(path="screenshot/orion-med_homepage.png")
        await page.close()

asyncio.run(main())