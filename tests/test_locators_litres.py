from playwright.sync_api import Page, expect

def test_locator_role_by_button(page: Page):
    page.goto("https://www.litres.ru/")                         # переходим по ссылке
    page.get_by_role("button", name="Найти").click()       # находим кнопку "Найти" и нажимаем
    expect(page.get_by_text("стивен кинг")).to_be_visible()     # проверяем текст в выпадающем списке на странице

def test_locator_placeholder_litres(page: Page):
    page.goto("https://www.litres.ru/")                                 # переходим по ссылке
    page.get_by_placeholder("Искать на Литрес").fill("иван крылов")     # вводим в поле поиска "Искать на Литрес" значение "иван крылов"
    page.keyboard.press("Enter")                                        # нажимаем ввод
    expect(page.get_by_text("Результаты поиска «иван крылов»"))         # проверяем текст на странице

def test_locator_role_by_datatest_id(page: Page):
    page.goto("https://www.litres.ru/")
    page.get_by_test_id("header-catalog-button").click()    # находим локатор catalog и нажимаем
    expect(page.get_by_text("Фанфики")).to_be_visible()     # проверяем текст на странице

