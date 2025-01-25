from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(autouse=True)            # создаем фикстуру, автоматически переводящую по ссылке в каждом тесте
def open_litres(page: Page):
    page.goto("https://orion-med.ru/")


def test_main_title(page: Page):
    assert page.title() == ("Орион Мед — оптовая продажа медицинских дезинфицирующих средств")

def test_instruments_page_title_by_role(page: Page):
    page.get_by_role(role="link", name="Для инструментов").click()
    expect(page).to_have_title("Для инструментов | Орион Мед")

def test_instruments_page_title_by_locator(page: Page):
    page.locator("xpath=//*[@id=\"app\"]/main/div/section[3]/div/div[1]/div/div/div/a[1]").click()
    expect(page).to_have_title("Для инструментов | Орион Мед")