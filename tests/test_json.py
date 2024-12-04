from taskmanager import TaskManager
from task import Task
import json


def test_save_to_json(tmp_path):
    """Проверяет сохранение задач в JSON-файл."""
    file_path = tmp_path / "tasks.json"
    manager = TaskManager(filename=str(file_path))
    manager.add_task(Task(
        1, "Тестовая задача", "Описание", "Тест", "2024-12-01", "высокий")
    )
    manager.save_to_json()

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        assert len(data) == 1
        assert data[0]["title"] == "Тестовая задача"
