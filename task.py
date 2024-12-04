from datetime import datetime


class Task:
    """
    Класс задач.
    Атрибуты: id, title, description, category, due_date, priority, status.
    """

    def __init__(
            self, task_id: int, title: str, description: str, category: str,
            due_date: str, priority: str, status: str = "Не выполнена"
    ):
        self.id = task_id
        self.title = title
        self.description = description
        self.category = category
        self.due_date = self.validate_date(due_date)
        self.priority = priority
        self.status = status

    def validate_date(self, date_str: str):
        """Проверяем формат даты."""
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Неверный формат даты. Используйте YYYY-MM-DD.")

    def to_dict(self):
        """Возвращаем задачу в виде словаря."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "due_date": self.due_date.strftime("%Y-%m-%d"),
            "priority": self.priority,
            "status": self.status,
        }
