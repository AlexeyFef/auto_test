from playwright.sync_api import Page, expect
import pytest


@pytest.fixture(autouse=True)      # создаем фикстуру, автоматически переводящую по ссылке в каждом тесте
def open_litres(page: Page):
    page.goto("https://orion-med.ru/")


def test_locator_role_by_link(page: Page):
    page.get_by_role("link", name="Доставка и оплата").click()  # ищем ссылку и нажимаем на ссылку
    expect(page).to_have_title("Адрес склада | Орион Мед")           # проверяем заголовок страницы


def test_locator_placeholder_orion(page: Page):
    page.get_by_placeholder("Искать дезсредство").fill("аламинол")  # ищем поле ввода и вводим значение
    page.keyboard.press("Enter")                                    # нажимаем ввод и переходим
    expect(page.get_by_text("аламинол"))                            # проверяем текст на странице
