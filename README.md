# Litestar - SQLModel - Alembic

![Listestar - SQLModel - Alembic](docs/py-litestar.png)

[![natorsc - py-litestar](https://img.shields.io/static/v1?label=natorsc&message=py-litestar&color=blue&logo=github)](https://github.com/natorsc/py-litestar)
[![stars - py-litestar](https://img.shields.io/github/stars/natorsc/py-litestar?style=social)](https://github.com/natorsc/py-litestar)
[![forks - py-litestar](https://img.shields.io/github/forks/natorsc/py-litestar?style=social)](https://github.com/natorsc/py-litestar)
[![License MIT](https://img.shields.io/static/v1?label=License&message=MIT&color=blue)](./LICENSE)

## ✨ Sobre este projeto

Um modelo inicial pronto para uso para a criação de aplicativos web com o framework Litestar e o SQLModel.

> estruturado, organizado e fácil de ampliar.

## 🛠 Tecnologias utilizadas

[![Python](https://img.shields.io/badge/-Python-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Litestar](https://img.shields.io/badge/-Litestar-blue?logo=litestar&logoColor=white)](https://github.com/litestar-org/litestar)
[![SQLModel](https://img.shields.io/badge/-SQLModel-blue?logo=sqlmodel&logoColor=white)](https://github.com/fastapi/sqlmodel)
[![Alembic](https://img.shields.io/badge/-Alembic-blue?logo=alembic&logoColor=white)](https://github.com/sqlalchemy/alembic)
[![Docker](https://img.shields.io/badge/-Docker-blue?logo=docker&logoColor=white)](https://github.com/docker)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

## 👨‍💻 Autor

Criado com 💙 por Renato Cruz. Tem alguma dúvida ou sugestão? Entre em contato a qualquer momento!

[![Email](https://img.shields.io/badge/-Email-blueviolet?logo=gmail&logoColor=white)](mailto:natorsc@gmail.com)

O que estou ouvindo enquanto programo ou estudo 😎🎵:

[![Spotify](https://img.shields.io/badge/-Spotify-darkgreen?logo=spotify&logoColor=white)](https://open.spotify.com/playlist/1xf3u29puXlnrWO7MsaHL5)

## 💡 Extra

Executar o projeto:

```bash
uvicorn py_litestar.app:app --reload
```

Ou

```bash
uv run server
```

### Documentação interativa

- ReDoc: http://localhost:8000/schema.
- Swagger UI: http://localhost:8000/schema/swagger.
- Stoplight Elements: http://localhost:8000/schema/elements.
- RapiDoc: http://localhost:8000/schema/rapidoc.

### Alembic

Sempre que houver alterações na tabelas executar:

```bash
uv run alembic revision --autogenerate -m "texto_da_alteração"
```

Para aplicar a alteração:

```bash
uv run alembic upgrade head
```

> Novas tabelas (models) devem ser importadas em `migrations/env.py`.

#### Erros

```bash
sa.Column('title', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
                   ^^^^^^^^
NameError: name 'sqlmodel' is not defined
```

Adicionar `import sqlmodel.sql.sqltypes  # noqa: F401` no arquivo de migração que foi gerado.
