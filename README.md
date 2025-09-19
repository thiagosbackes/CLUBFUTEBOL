# CLUBFUTEBOL - MVP Demo

Protótipo do web app CLUBFUTEBOL para validação da jornada inicial.

## Funcionalidades incluídas
- Landing page com capa estilo "camisa 10" e box de login/cadastro.
- Autenticação simulada (login como presidente ou atleta).
- Dashboard simples com clubes e carteirinha mock.

## Como rodar localmente
```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py
flask --app app run --debug
```
Abra http://127.0.0.1:5000
```

## Deploy no Render
- Suba este repositório no GitHub
- No Render, crie um novo Web Service apontando para este repositório
- Ele vai rodar usando o Procfile já configurado
