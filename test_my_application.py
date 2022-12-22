import re
from playwright.sync_api import Page, expect


def test_homepage_has_Playwright_in_title_and_get_started_link_linking_to_the_intro_page(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

    # create a locator
    get_started = page.get_by_role("link", name="Get started")

    # Expect an attribute "to be strictly equal" to the value.
    expect(get_started).to_have_attribute("href", "/docs/intro")

    # Click the get started link.
    get_started.click()

    # Expects the URL to contain intro.
    expect(page).to_have_url(re.compile(".*intro"))


def test_add_to_cart(page:Page):
    page.goto('https://www.demoblaze.com/index.html')
    expect(page).to_have_title('STORE')
    page.get_by_role("link", name="Samsung galaxy s6").click()
    expect(page.get_by_text("Add to cart")).to_be_visible()
    page.get_by_text('Add to cart').click()

def test_login(page:Page):
    page.goto('https://www.demoblaze.com/index.html')
    page.get_by_role("link", name="Log in").click() #get_by_text("Log in").nth(1)
    # page.get_by_test_id('#loginusername').type('Kate')
    page.locator('#loginusername').type('KateFox1')
    page.locator('#loginpassword').type('KateFox')
    page.get_by_role('button').click()