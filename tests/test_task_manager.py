import pytest
from task import Task
from taskmanager import TaskManager


@pytest.fixture
def sample_task():
    """Возвращает пример задачи."""
    return Task(
        task_id=1,
        title="Тестовая задача",
        description="Описание тестовой задачи",
        category="Тест",
        due_date="2024-12-01",
        priority="высокий"
    )


@pytest.fixture
def task_manager():
    """Возвращает менеджер задач с предварительно загруженной задачей."""
    manager = TaskManager()
    manager.add_task(Task(
        task_id=1,
        title="Название",
        description="Описание",
        category="Категория",
        due_date="2024-12-04",
        priority="высокий"
    ))
    return manager


def test_add_task(task_manager, sample_task):
    """Проверяет добавление задачи."""
    initial_count = len(task_manager.tasks)
    new_task = Task(
        task_id=2,
        title="Вторая задача",
        description="Описание второй задачи",
        category="Работа",
        due_date="2024-12-02",
        priority="средний"
    )
    task_manager.add_task(new_task)
    assert len(task_manager.tasks) == initial_count + 1
    assert task_manager.tasks[-1].title == "Вторая задача"


def test_complete_task(task_manager):
    """Проверяет выполнение задачи."""
    task_manager.edit_task(task_id=1, status="Выполнена")
    assert task_manager.tasks[0].status == "Выполнена"


def test_find_tasks_by_keyword(task_manager):
    """Проверяет поиск задачи по ключевому слову."""
    results = task_manager.find_tasks(keyword="Название")
    assert len(results) == 1
    assert results[0].title == "Название"


def test_find_tasks_by_category(task_manager):
    """Проверяет поиск задачи по категории."""
    results = task_manager.find_tasks(category="Категория")
    assert len(results) == 1
    assert results[0].category == "Категория"


def test_find_tasks_by_status(task_manager):
    """Проверяет поиск задачи по статусу."""
    results = task_manager.find_tasks(status="Не выполнена")
    assert len(results) == 1
    assert results[0].status == "Не выполнена"


def test_delete_task(task_manager):
    """Проверяет удаление задачи по ID."""
    initial_count = len(task_manager.tasks)
    task_manager.delete_task(task_id=1, category="Работа")
    assert len(task_manager.tasks) == initial_count - 1
    assert not any(task.id == 1 for task in task_manager.tasks)
