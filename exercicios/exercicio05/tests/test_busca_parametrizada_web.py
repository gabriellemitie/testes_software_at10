import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture
def chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.mark.parametrize("termo_busca", [
    "Python",
    "Selenium",
    "Pytest",
    "API Testing",
    "Automation",
])
def test_busca_google(chrome_driver, termo_busca):
    driver = chrome_driver
    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(termo_busca)
    search_box.submit()
    time.sleep(2)

    assert termo_busca.lower() in driver.page_source.lower()