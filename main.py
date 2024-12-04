from taskmanager import TaskManager
from task import Task


def print_menu():
    """Вывод меню."""
    print("\nМенеджер задач")
    print("1. Просмотреть задачи")
    print("2. Добавить задачу")
    print("3. Изменить задачу")
    print("4. Отметить задачу как выполненную")
    print("5. Удалить задачу")
    print("6. Найти задачи")
    print("7. Сохранить данные в JSON")
    print("8. Выход")


def main():
    manager = TaskManager()

    while True:
        print_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            tasks = manager.tasks
            if tasks:
                for task in tasks:
                    print(task.to_dict())
            else:
                print("Список задач пуст.")

        elif choice == "2":
            try:
                task_id = len(manager.tasks) + 1
                title = input("Название: ")
                description = input("Описание: ")
                category = input("Категория: ")
                due_date = input("Срок выполнения (YYYY-MM-DD): ")
                priority = input("Приоритет (низкий/средний/высокий): ")
                task = Task(
                    task_id, title, description, category, due_date, priority
                )
                manager.add_task(task)
                print("Задача успешно добавлена.")
            except ValueError as err:
                print(err)

        elif choice == "3":
            task_id = int(input("Введите ID задачи для изменения: "))
            title = input("Новое название: ")
            description = input("Новое описание: ")
            category = input("Новая категория: ")
            due_date = input("Новый срок выполнения (YYYY-MM-DD): ")
            priority = input("Новый приоритет (низкий/средний/высокий): ")
            try:
                manager.edit_task(
                    task_id, title=title, description=description,
                    category=category, due_date=due_date, priority=priority
                )
                print("Задача успешно обновлена.")
            except ValueError as err:
                print(err)

        elif choice == "4":
            task_id = int(input("Введите ID задачи: "))
            try:
                manager.edit_task(task_id, status="Выполнена")
                print("Задача отмечена как выполненная.")
            except ValueError as err:
                print(err)

        elif choice == "5":
            task_id = int(input("Введите ID задачи для удаления: "))
            category = input("Введите категорию (Опционально): ")
            manager.delete_task(task_id, category=category or None)
            print("Задача успешно удалена.")

        elif choice == "6":
            keyword = input("Ключевое слово: ")
            category = input("Категория: ")
            status = input("Статус (Выполнена/Не выполнена): ")
            tasks = manager.find_tasks(
                keyword=keyword, category=category, status=status)
            if tasks:
                for task in tasks:
                    print(task.to_dict())
            else:
                print("Подходящих задач не найдено.")

        elif choice == "7":
            manager.save_to_json()
            print("Задачи сохранены в JSON-файл.")

        elif choice == "8":
            print("Выход из Менеджера задач.")
            break
        else:
            print("Ошибка, выберите один из доступных вариантов.")


if __name__ == "__main__":
    main()
