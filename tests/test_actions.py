from playwright.sync_api import Page, expect

def test_main_actions(page: Page):
    page.get_by_test_id("search__input").fill(("python"))   # вводим в поле поиска "Искать на Литрес" значение "python"
    page.keyboard.press("Enter")                            # нажимаем ввод

    expect(page).to_have_url("https://www.litres.ru/search/?q=python")  # проверяем URL
    page.locator("xpath=//*[@aria-description='Книги, которые можно читать без ограничений с активной Литрес: "
                 "Подпиской']").click()               # по xpath находим и переключаем switcher "Доступно по подписке"
    page.locator("xpath=//*[@aria-description='Книги, которые можно взять по Литрес: Абонементу']").click()
            #  по xpath находим и переключаем switcher "Доступно в абонементе"

    # page.locator("xpath=//*[@id='languages-ru']").check(force=True)
    page.check("label[for='languages-ru']")             # включаем checkbox "Русский"

    page.locator("button:has-text('Принять')").click()  # принимаем соглашение о cockies

    page.pause()                                        # поставить на паузу для просмотра результата
