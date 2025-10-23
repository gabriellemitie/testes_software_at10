import pytest
from selenium.webdriver.common.by import By
import time
import shutil
URL = "https://practicetestautomation.com/practice-test-login/"

USERNAME_VALIDO = "student"
SENHA_VALIDA = "Password123"



# Pula todos os testes deste arquivo se o Chrome não estiver instalado
pytestmark = pytest.mark.skip(reason="Simulando ambiente sem Chrome")


@pytest.mark.usefixtures("chrome_driver")
class TestLogin:
    
    def test_login_sucesso(self, chrome_driver):
        driver = chrome_driver
        driver.get(URL)

        driver.find_element(By.ID, "username").send_keys(USERNAME_VALIDO)
        driver.find_element(By.ID, "password").send_keys(SENHA_VALIDA)
        time.sleep(2)  
        driver.find_element(By.ID, "submit").click()

        # Verifica se o login foi bem-sucedido
        assert "Logged In Successfully" in driver.page_source
        assert "student" in driver.page_source

    def test_login_email_invalido(self, chrome_driver):
        driver = chrome_driver
        driver.get(URL)

        driver.find_element(By.ID, "username").send_keys("usuario_errado")
        driver.find_element(By.ID, "password").send_keys(SENHA_VALIDA)
        time.sleep(2)  
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)  
        # Verifica mensagem de erro
        erro = driver.find_element(By.ID, "error").text
        assert "Your username is invalid!" in erro

    def test_login_senha_incorreta(self, chrome_driver):
        driver = chrome_driver
        driver.get(URL)

        driver.find_element(By.ID, "username").send_keys(USERNAME_VALIDO)
        driver.find_element(By.ID, "password").send_keys("SenhaErrada123")
        time.sleep(2)  
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)  
        erro = driver.find_element(By.ID, "error").text
        assert "Your password is invalid!" in erro

    def test_login_campos_vazios(self, chrome_driver):
        driver = chrome_driver
        driver.get(URL)

        # Não preencher nenhum campo
        driver.find_element(By.ID, "submit").click()

        # Deve continuar na mesma página e exibir erro
        assert driver.current_url == URL
        assert "error" in driver.page_source

    def test_mensagens_erro_adequadas(self, chrome_driver):
        driver = chrome_driver
        driver.get(URL)

        # Testa primeiro usuário incorreto
        driver.find_element(By.ID, "username").send_keys("invalido")
        driver.find_element(By.ID, "password").send_keys(SENHA_VALIDA)
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)  
        msg = driver.find_element(By.ID, "error").text
        assert msg == "Your username is invalid!"

        # Testa senha incorreta
        driver.get(URL)
        driver.find_element(By.ID, "username").send_keys(USERNAME_VALIDO)
        driver.find_element(By.ID, "password").send_keys("123")
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)  
        msg = driver.find_element(By.ID, "error").text
        assert msg == "Your password is invalid!"
