import uvicorn
from litestar import Litestar
from litestar.config.cors import CORSConfig
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.static_files import StaticFilesConfig
from litestar.template.config import TemplateConfig

from py_litestar.controllers import TaskController, index

cors_config = CORSConfig(allow_origins=["*"])

app = Litestar(
    route_handlers=[TaskController, index],
    template_config=TemplateConfig(
        directory="templates",
        engine=JinjaTemplateEngine,
    ),
    static_files_config=[
        StaticFilesConfig(
            path="/static",
            directories=["static"],
        )
    ],
    cors_config=cors_config,
)


def start() -> None:
    uvicorn.run("py_litestar.app:app", host="127.0.0.1", port=8000, reload=True)
