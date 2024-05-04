import pytest
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    chrome_browser = webdriver.Chrome(ChromeDriverManager().install())
    chrome_browser.implicitly_wait(10)
    chrome_browser.maximize_window()
    return chrome_browser



def randomize_list(self):
    return random.choice(self)
