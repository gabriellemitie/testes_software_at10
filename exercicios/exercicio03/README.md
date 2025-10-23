
**Arquivo:** `exercicios/tests/test_todos_crud.py`
# ✅ Testes de API — JSONPlaceholder (CRUD de Todos)

## 🎯 Objetivo
Validar o funcionamento do endpoint `/todos` da [JSONPlaceholder API](https://jsonplaceholder.typicode.com/).

São testadas todas as operações CRUD:
- **CREATE** (POST)
- **READ** (GET)
- **UPDATE** (PATCH)
- **DELETE** (DELETE)
- **VERIFY** (GET após exclusão)

---

## ⚙️ Tecnologias
- Python 3.12+
- pytest
- requests

---

## 🧩 Estrutura esperada de um TODO
```json
{
  "userId": 1,
  "id": 1,
  "title": "Minha tarefa",
  "completed": false
}  
``` 

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
pytest -v exercicios/exercicio03/test_todos_crud.py
```

## ✅ Resultados esperados  

5 tests passed (dependendo da parametrização)
Tempo: ~1–2 segundos
