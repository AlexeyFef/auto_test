from playwright.sync_api import Page, expect

def test_locator_role_by_link(page: Page):
    page.goto("https://orion-med.ru/")                               # переходим по ссылке
    page.get_by_role("link", name="Доставка и оплата").click()  # ищем ссылку и нажимаем на ссылку
    expect(page).to_have_title("Адрес склада | Орион Мед")           # проверяем заголовок страницы

def test_locator_placeholder_orion(page: Page):
    page.goto("https://orion-med.ru/")                              # переходим по ссылке
    page.get_by_placeholder("Искать дезсредство").fill("аламинол")  # ищем поле ввода и вводим значение
    page.keyboard.press("Enter")                                    # нажимаем ввод и переходим
    expect(page.get_by_text("аламинол"))                            # проверяем текст на странице

def test_locator_role_by_button(page: Page):
    page.goto("https://www.litres.ru/")
    page.get_by_role("button", name="Найти").click()
    expect(page.get_by_text("стивен кинг")).to_be_visible()

def test_locator_placeholder_litres(page: Page):
    page.goto("https://www.litres.ru/")
    page.get_by_placeholder("Искать на Литрес").fill("иван крылов")
    page.keyboard.press("Enter")
    expect(page.get_by_text("Результаты поиска «иван крылов»"))
