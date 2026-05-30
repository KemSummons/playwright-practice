import datetime
import time
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://demoqa.com/automation-practice-form")

    page.fill('input[id="firstName"]', 'Кени Вест')
    page.type('input[id="lastName"]', 'Пушкин')
    page.fill('input[id="userEmail"]', 'keny@west.com')
    page.check('#gender-radio-3')
    page.fill('input[id="userNumber"]', '1234567890')

    today_formatted = datetime.date.today().strftime("%d %b %Y")
    expect(page.locator('#dateOfBirthInput')).to_have_value(today_formatted)
    date_input = page.locator("#dateOfBirthInput")

    date_input.click()
    date_input.press("Control+A")
    date_input.fill("25 Jan 1994")
    date_input.press("Enter")

    subjects_input = page.locator('#subjectsInput')
    subjects_input.click()
    subjects_input.fill("Math")
    subjects_input.press('Enter')
    subjects_input.fill('English')
    subjects_input.press('Enter')

    page.check('#hobbies-checkbox-2')
    page.check('#hobbies-checkbox-3')
    page.locator("#uploadPicture").set_input_files("cat.jpg")
    page.fill('#currentAddress', 'Улица Пушкина, дом Колотушкина')

    page.locator("#react-select-3-input").click()
    page.get_by_text("Haryana").click()
    page.locator("#react-select-4-input").click()
    page.get_by_text("Karnal").click()

    expect(page.locator("footer")).to_have_text("© 2013-2026 TOOLSQA.COM | ALL RIGHTS RESERVED.")
    page.locator('#submit').click()

def test_active_elements(page: Page) -> None:
    page.goto("https://demoqa.com/radio-button")
    assert page.is_enabled("#yesRadio")
    assert page.is_enabled("#impressiveRadio")
    assert not page.is_enabled("#noRadio")

def test_visible_elements(page: Page) -> None:
    page.goto("https://demoqa.com/checkbox")
    expect(page.locator(".rc-tree-title", has_text="Home")).to_be_visible()
    expect(page.locator(".rc-tree-title", has_text="Desktop")).not_to_be_visible()
    page.click('.rc-tree-switcher.rc-tree-switcher_close')
    expect(page.locator(".rc-tree-title", has_text="Desktop")).to_be_visible()

def test_long_visible(page: Page) -> None:
    page.goto("https://demoqa.com/dynamic-properties")
    expect(page.locator('#visibleAfter')).not_to_be_visible()
    page.wait_for_selector('#visibleAfter', state='visible', timeout=6000)
