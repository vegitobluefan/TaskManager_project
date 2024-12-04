import json


class TaskManager:
    """Класс для управления задачами."""

    def __init__(self, filename: str = "tasks.json"):
        self.tasks: list = []
        self.filename = filename

    def save_to_json(self):
        """Сохраняет задачи в файл JSON."""
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(
                    [task.to_dict() for task in self.tasks], file,
                    ensure_ascii=False, indent=4
                )
        except IOError as err:
            raise IOError(f"Ошибка в {self.filename}: {err}")

    def add_task(self, task):
        """Добавление задачи."""
        self.tasks.append(task)

    def delete_task(self, task_id: int, category: str):
        """Удаление задачи по id."""
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.tasks = [task for task in self.tasks if task.category != category]

    def find_tasks(self, keyword: str = None, category: str = None, status: str = None):
        """Ищет задачи по ключевому слову, категории или статусу."""
        return [
            task for task in self.tasks
            if (
                not keyword or keyword.lower() in task.title.lower()
                or keyword.lower() in task.description.lower()
            )
            and (not category or task.category == category)
            and (not status or task.status == status)
        ]

    def edit_task(self, task_id: int, **kwargs):
        """Редактирование задачи по id."""
        for task in self.tasks:
            if task.id == task_id:
                for key, value in kwargs.items():
                    if hasattr(task, key) and value is not None:
                        setattr(task, key, value)
                return
        raise ValueError(f"Задача с ID {task_id} не найдена.")
