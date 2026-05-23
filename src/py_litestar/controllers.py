from litestar import Controller, delete, get, post, put
from litestar.exceptions import NotFoundException
from litestar.response import Template
from sqlmodel import select

from py_litestar.database import get_session
from py_litestar.models import Task


@get("/", sync_to_thread=False)
def index() -> Template:
    return Template(template_name="index.html")


class TaskController(Controller):
    path = "/tasks"

    @get()
    async def list_tasks(self) -> list[Task]:
        """Retorna todas as tarefas."""
        with get_session() as session:
            return session.exec(select(Task)).all()

    @post()
    async def create_task(self, data: Task) -> Task:
        """Cria uma nova tarefa."""
        with get_session() as session:
            session.add(data)
            session.commit()
            session.refresh(data)
            return data

    @get(path="/{task_id:int}")
    async def get_task(self, task_id: int) -> Task:
        """Busca uma tarefa específica pelo ID."""
        with get_session() as session:
            task = session.get(Task, task_id)
            if not task:
                raise NotFoundException(detail=f"Task com id {task_id} não encontrada")
            return task

    @put(path="/{task_id:int}")
    async def update_task(self, task_id: int, data: Task) -> Task:
        """Atualiza uma tarefa existente."""
        with get_session() as session:
            task = session.get(Task, task_id)
            if not task:
                raise NotFoundException(detail=f"Task com id {task_id} não encontrada")
            task.title = data.title
            task.done = data.done
            session.commit()
            session.refresh(task)
            return task

    @delete(path="/{task_id:int}")
    async def delete_task(self, task_id: int) -> None:
        """Remove uma tarefa."""
        with get_session() as session:
            task = session.get(Task, task_id)
            if not task:
                raise NotFoundException(detail=f"Task com id {task_id} não encontrada")
            session.delete(task)
            session.commit()
