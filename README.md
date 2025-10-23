# Afiliados Tech

Plataforma web em **Python (FastAPI)*** para exibir produtos relacionados a tecnologia vindos de fontes externas (afiliados).

## Recursos
- Listagem dinâmica de produtos sem recarregar a página
- Login com conta Google
- Histórico de visualizações e relatórios
- Comparativo de preços e variação de valor

## Tecnologias
- **Backend:** FastAPI
- **Banco:** SQLite (padrão)
- **Frontend:** HTML + CSS + JS (dinãmico com fetch)
- **Login:** Google OAuth via Authlib

## Estrutura
```bash
app/
|---routes/
|---models/
|---services/
|---db/
|---templates/
|---static/
