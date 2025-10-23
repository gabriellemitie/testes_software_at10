import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/todos"

# -------------------------------
# FIXTURE: criação de dado de teste
# -------------------------------
@pytest.fixture
def novo_todo():
    """Cria um novo TODO para usar nos testes"""
    payload = {
        "title": "Minha tarefa",
        "completed": False,
        "userId": 1
    }
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 201  # criado com sucesso

    todo = response.json()
    yield todo  # passa para o teste

    # -------------------------------
    # TEARDOWN (limpeza)
    # -------------------------------
    delete_resp = requests.delete(f"{BASE_URL}/{todo['id']}")
    assert delete_resp.status_code in [200, 204]


# -------------------------------
# TESTES CRUD
# -------------------------------

def test_create_todo():
    """Teste de criação de TODO (POST)"""
    payload = {
        "title": "Minha tarefa",
        "completed": False,
        "userId": 1
    }
    response = requests.post(BASE_URL, json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Minha tarefa"
    assert data["completed"] is False
    assert data["userId"] == 1
    assert "id" in data


def test_read_todo():
    """Teste de leitura de TODO existente (GET)"""
    response = requests.get(f"{BASE_URL}/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    assert "completed" in data


def test_update_todo(novo_todo):
    """Teste de atualização parcial (PATCH)"""
    todo_id = novo_todo["id"]
    patch_payload = {"completed": True}

    response = requests.patch(f"{BASE_URL}/{todo_id}", json=patch_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["completed"] is True


def test_delete_todo(novo_todo):
    """Teste de exclusão (DELETE)"""
    todo_id = novo_todo["id"]
    response = requests.delete(f"{BASE_URL}/{todo_id}")
    assert response.status_code in [200, 204]


def test_verify_todo_deletion():
    """Verifica se um TODO inexistente retorna vazio ou 404"""
    response = requests.get(f"{BASE_URL}/9999999")
    assert response.status_code in [200, 404]
    data = response.json()
    # Alguns retornam {} ao invés de 404
    assert isinstance(data, (dict, list))
