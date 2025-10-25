import requests


class UsersAPI:

    def __init__(self, base_url="https://jsonplaceholder.typicode.com", session=None):
        self.base_url = base_url.rstrip("/")
        self.session = session or requests.Session()
        self.endpoint = f"{self.base_url}/users"

    def listar_usuarios(self):
        resp = self.session.get(self.endpoint)
        resp.raise_for_status()
        return resp.json()

    def buscar_usuario_por_email(self, email):
        # Busca usuário(s) por email. Retorna lista (pode ser vazia).
        # JSONPlaceholder aceita query params como `?email=...`.
        resp = self.session.get(self.endpoint, params={"email": email})
        resp.raise_for_status()
        return resp.json()
