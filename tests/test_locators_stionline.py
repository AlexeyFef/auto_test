from playwright.sync_api import Page, expect
import pytest


@pytest.fixture(autouse=True)  # создаем фикстуру, автоматически переводящую по ссылке в каждом тесте
def open_litres(page: Page):
    page.goto("https://stionline.ru/")


def test_locator_role_by_img_and_placeholder(page: Page):
    page.get_by_role("img", name="поиск").click()       # находим значок лупа для поиска и нажимаем
    page.get_by_placeholder("Поиск").fill("racestyptine")    # ищем поле ввода и вводим значение
    page.keyboard.press("Enter")                             # нажимаем ввод и переходим
    expect(page.get_by_text("Гемостатические препараты"))    # проверяем текст на странице


def test_locator_role_by_alttext(page: Page):
    page.goto("https://stionline.ru/info/brands/")
    page.get_by_alt_text("STIOnline").click()               # находим иконку (логотип) и нажимаем
    expect(page).to_have_url("https://stionline.ru/")       # проверяем URL страницы
