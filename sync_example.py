from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://stident.ru/")
    page.screenshot(path="screenshot/stident_homepage.png")
    page.close()

