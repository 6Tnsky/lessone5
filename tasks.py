class Task:
    def __init__(self, description, deadline, completed=False):
        self.description = description
        self.deadline = deadline
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def show_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.completed]
        if not current_tasks:
            print("Нет текущих задач.")
        else:
            for i, task in enumerate(current_tasks, start=1):
                print(f"{i}. {task}")

    def complete_task(self, task_number):
        try:
            # Получаем индекс задачи в списке невыполненных задач
            current_tasks = [task for task in self.tasks if not task.completed]
            task_to_complete = current_tasks[task_number - 1]
            # Помечаем задачу как выполненную
            task_to_complete.mark_completed()
            print(f"Задача '{task_to_complete.description}' отмечена как выполненная.")
        except IndexError:
            print("Неправильный номер задачи. Пожалуйста, попробуйте снова.")


# Тест
manager = TaskManager()
manager.add_task("Купить продукты", "2023-10-15")
manager.add_task("Сделать домашнее задание", "2023-10-16")

print("Текущие задачи:")
manager.show_current_tasks()

# Выполним первую задачу
print("\nВыполнение задачи 1")
manager.complete_task(1)

print("\nТекущие задачи после выполнения:")
manager.show_current_tasks()