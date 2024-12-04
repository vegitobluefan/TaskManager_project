import pytest
from task import Task


def test_task_creation():
    """Проверяет создание задачи с корректными данными."""
    task = Task(
        task_id=1,
        title="Название задачи",
        description="Описание задачи",
        category="Категория задачи",
        due_date="2024-12-04",
        priority="Приоритет задачи"
    )
    assert task.id == 1
    assert task.title == "Название задачи"
    assert task.description == "Описание задачи"
    assert task.category == "Категория задачи"
    assert task.due_date.strftime("%Y-%m-%d") == "2024-12-04"
    assert task.priority == "Приоритет задачи"
    assert task.status == "Не выполнена"


def test_invalid_due_date():
    """Проверяет обработку неправильной даты."""
    with pytest.raises(ValueError):
        Task(
            task_id=1,
            title="Неверная задача",
            description="Задача с неправильной датой",
            category="Тест",
            due_date="31-12-2024",
            priority="средний"
        )
