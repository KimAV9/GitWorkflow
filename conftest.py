from selenium import webdriver
import pytest
import random
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    options = Options()
    options.add_argument('--headless')
    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.implicitly_wait(10)
    chrome_browser.maximize_window()
    return chrome_browser


def randomize_list(self):
    return random.choice(self)
