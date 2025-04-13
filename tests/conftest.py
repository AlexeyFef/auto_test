from playwright.sync_api import Page, expect
import pytest


@pytest.fixture(autouse=True)  # создаем фикстуру, автоматически переводящую по ссылке в каждом тесте
def open_litres(page: Page):
    page.goto("https://www.litres.ru/")
    expect(page).to_have_url("https://www.litres.ru/")  # проверка, что перешли точно по ссылке
