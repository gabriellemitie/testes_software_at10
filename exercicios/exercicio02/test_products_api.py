import pytest
import requests

BASE_URL = "https://fakestoreapi.com"

# Schema esperado para um produto
PRODUCT_SCHEMA_KEYS = [
    "id",
    "title",
    "price",
    "description",
    "category",
    "image"
]

# Categorias válidas conhecidas
CATEGORIES = ["electronics"]
# -------------------------------
# TESTES DE API
# -------------------------------

def test_listar_todos_os_produtos():
    """Verifica se a API retorna todos os produtos corretamente"""
    response = requests.get(f"{BASE_URL}/products")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0
    # Verifica se todos os produtos têm as chaves esperadas
    for produto in data:
        for key in PRODUCT_SCHEMA_KEYS:
            assert key in produto, f"Chave '{key}' ausente em {produto}"


def test_buscar_produto_por_id():
    """Busca um produto específico pelo ID"""
    produto_id = 1
    response = requests.get(f"{BASE_URL}/products/{produto_id}")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)
    assert data["id"] == produto_id
    for key in PRODUCT_SCHEMA_KEYS:
        assert key in data


@pytest.mark.parametrize("categoria", CATEGORIES)
def test_filtrar_produtos_por_categoria(categoria):
    """Filtra produtos por categoria e valida retorno"""
    response = requests.get(f"{BASE_URL}/products/category/{categoria}")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert all(prod["category"] == categoria for prod in data), f"Categoria incorreta em {data}"


def test_validar_schema_produto():
    """Valida o schema de um produto específico"""
    response = requests.get(f"{BASE_URL}/products/5")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)
    assert set(PRODUCT_SCHEMA_KEYS).issubset(data.keys())


def test_limite_de_produtos_retornados():
    """Testa se o endpoint com limite retorna o número correto de produtos"""
    limite = 3
    response = requests.get(f"{BASE_URL}/products?limit={limite}")
    data = response.json()

    assert response.status_code == 200
    assert len(data) == limite, f"Esperado {limite}, retornado {len(data)}"
    for produto in data:
        for key in PRODUCT_SCHEMA_KEYS:
            assert key in produto
