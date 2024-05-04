import pytest
from pages.auth_page import AuthPage


def test_auth(browser):
    auth_page = AuthPage(browser)
    auth_page.open()

    auth_page.username_click()
    auth_page.username_send()

    auth_page.password_click()
    auth_page.password_send()

    auth_page.login_button()
    auth_page.login_button_click()
