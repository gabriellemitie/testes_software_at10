import pytest
import requests


# Parte A: validação de emails (REST)
emails_invalidos = [
    "sem-arroba.com",
    "@sem-usuario.com",
    "sem-dominio@",
    "espacos no meio@teste.com",
    "caracteres!especiais@teste.com",
    "..pontos@teste.com",
    "teste@",
    "@teste.com",
]


@pytest.mark.parametrize("email_invalido", emails_invalidos)
def test_validacao_email_api(email_invalido):
    response = requests.post(
        "https://reqres.in/api/register",
        json={"email": email_invalido, "password": "senha123"},
    )

    # reqres.in can return 400 or 401 for invalid inputs; accept both to be robust
    assert response.status_code in (400, 401)


# Parte B: validação de senhas (REST)
senhas_invalidas = [
    ("123", "muito curta"),
    ("semNumero", "sem número"),
    ("semmaiuscula123", "sem maiúscula"),
    ("12345678", "só números"),
    ("ab", "muito curta"),
]


@pytest.mark.parametrize("senha,motivo", senhas_invalidas)
def test_validacao_senha_api(senha, motivo):
    response = requests.post(
        "https://reqres.in/api/register",
        json={"email": "test@test.com", "password": senha},
    )

    # reqres.in can return 400 or 401 for invalid inputs; accept both to be robust
    assert response.status_code in (400, 401)