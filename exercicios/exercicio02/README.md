
**Arquivo:** `exercicios/tests/test_products_api.py`

# 🛒 Testes Automatizados — FakeStoreAPI

## 🎯 Objetivo
Testar o endpoint `/products` da [FakeStoreAPI](https://fakestoreapi.com/) validando o comportamento das principais operações de leitura e filtragem.

---

## 🧪 Testes implementados
- Listar todos os produtos
- Buscar produto por ID
- Filtrar produtos por categoria (`electronics`)
- Validar o schema da resposta
- Testar limite de produtos retornados (`?limit=`)

---

## ⚙️ Tecnologias
- Python 3.12+
- pytest
- requests

---

## 📦 Instalação

Crie e ative o ambiente virtual:
```bash
python -m venv venv
.\venv\Scripts\activate
``` 
Instale as dependências  
```bash
pip install -r requirements.txt  
```

## ▶️ Execução dos testes

Para rodar todos os testes:  
```bash  
pytest -v exercicios/exercicio02/test_products_api.py
```

## ✅ Resultados esperados  

5 tests passed (dependendo da parametrização)
Tempo: ~1–2 segundos
