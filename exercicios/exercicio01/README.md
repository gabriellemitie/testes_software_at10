# 🧠 Teste Automatizado — Formulário de Login (Selenium)

## 🎯 Objetivo
Automatizar testes para o formulário de login do site [Practice Test Automation](https://practicetestautomation.com/practice-test-login/).

Os testes verificam:
- Login com credenciais válidas  
- Login com email inválido  
- Login com senha incorreta  
- Tentativa de login com campos vazios  
- Mensagens de erro apropriadas

---

## ⚙️ Tecnologias
- Python 3.12+
- pytest
- selenium
- webdriver-manager

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
pytest -v exercicios/exercicio01/test_login.py
```
Se o Google Chrome não estiver instalado, os testes serão automaticamente pulados (skipped).

Para ver o motivo dos skips:  
```bash 
pytest -rs
``` 

## ✅ Resultados esperados  
5 tests skipped (Chrome não instalado)
Tempo: ~1–2 segundos


Se o Chrome estiver instalado:

5 tests passed (Selenium Web)
Tempo: ~50 a 60 segundos
