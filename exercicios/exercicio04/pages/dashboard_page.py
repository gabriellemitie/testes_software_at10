from pages.base_page import BasePage


class DashboardPage(BasePage):

    def esta_logado(self):
        try:
    
            return "Logged In Successfully" in self.driver.page_source
        except Exception:
            return False

    def obter_mensagem_boas_vindas(self):
        try:
            return self.driver.page_source
        except Exception:
            return ""