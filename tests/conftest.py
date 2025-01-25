from playwright.sync_api import Page
import pytest


@pytest.fixture(autouse=True)  # создаем фикстуру, автоматически переводящую по ссылке в каждом тесте
def open_litres(page: Page):
    page.goto("https://www.litres.ru/")
