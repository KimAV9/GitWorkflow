from selenium import webdriver
import pytest
import random


@pytest.fixture
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    chrome_browser.maximize_window()
    return chrome_browser


def randomize_list(self):
    return random.choice(self)
