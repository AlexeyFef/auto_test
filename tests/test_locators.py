from playwright.sync_api import Page, expect

def test_locator_role(page: Page):
    page.goto("https://orion-med.ru/")
    page.get_by_role("link", name="Доставка и оплата").click()
    expect(page).to_have_title("Адрес склада | Орион Мед")