from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture
def chrome_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
