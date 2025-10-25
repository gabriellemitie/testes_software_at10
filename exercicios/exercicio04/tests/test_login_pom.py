import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


USERNAME_VALIDO = "student"
SENHA_VALIDA = "Password123"


@pytest.mark.usefixtures("chrome_driver")
class TestLoginPOM:

    def test_login_sucesso(self, chrome_driver):
        login = LoginPage(chrome_driver)
        dashboard = DashboardPage(chrome_driver)

        login.abrir()
        login.fazer_login(USERNAME_VALIDO, SENHA_VALIDA)

        assert dashboard.esta_logado(), "Usuário não foi autenticado com sucesso"
        assert USERNAME_VALIDO in dashboard.obter_mensagem_boas_vindas()
