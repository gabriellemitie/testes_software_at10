from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir(self, url):
        self.driver.get(url)

    def clicar(self, locator):
        elemento = self.wait.until(EC.element_to_be_clickable(locator))
        elemento.click()

    def digitar(self, locator, texto):
        campo = self.wait.until(EC.visibility_of_element_located(locator))
        campo.clear()
        campo.send_keys(texto)

    def obter_texto(self, locator):
        elemento = self.wait.until(EC.visibility_of_element_located(locator))
        return elemento.text
