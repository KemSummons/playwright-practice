from playwright.sync_api import Page, expect
import time


def test_text_box(page: Page):
    page.goto('https://dev-cinescope.coconutqa.ru/register')

    page.fill('input[name="fullName"]', 'Пушкин Кени Вест')
    page.fill('input[name="email"]', 'test@qa.com')
    page.fill('input[name="password"]', 'qwerty123Q')
    page.fill('input[name="passwordRepeat"]', 'qwerty123Q')
    page.get_by_role("button", name="Зарегистрироваться").click()

    expect(page.locator('#output #name')).to_have_text('Name: Пушкин Кени Вест')
    expect(page.locator('#output #email')).to_have_text('Email: test@qa.com')
    expect(page.locator('#output #password')).to_have_text('Current Address :qwerty123Q')
    expect(page.locator('#output #passwordRepeat')).to_have_text('Permananet Address :Moscow, Mashkova 1')
