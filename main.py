#Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных)
# задач.

# Добавлен класс Task
class Task:
    def __init__(self, description, deadline, status):
        self.description = description
        self.deadline = deadline
        self.status = status

# Добавлен метод __str__ для получения информации о задаче
    def __str__(self):
        return f"Описание: {self.description}, Срок выполнения: {self.deadline}, Статус: {self.status}"

# Добавлен класс TaskManager Для управления задачами
class TaskManager:
    def __init__(self):
        self.tasks = []

# Добавлен метод add_task для добавления задач
    def add_task(self):
        description = input("Введите описание задачи: ")
        deadline = input("Введите срок выполнения задачи: ")
        status = input("Введите статус задачи (выполнено/не выполнено): ")
        task = Task(description, deadline, status)
        self.tasks.append(task)
        print("Задачи добавлены.")

# Добавлен метод task_completed для отметки выполненных задач
    def task_completed(self):
        if self.tasks:
            task_index = int(input("Введите номер задачи которая выполнена: ")) - 1
            if 0 <= task_index < len(self.tasks):
                self.tasks[task_index].status = "Выполнено"
                print("Задача отмечена как выполненная.")
            else:
                print("Неверный номер задачи.")

# Добавлен метод show_tasks для вывода списка текущих (выполненных/не выполненных) задач
    def show_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

# Использование
task_manager = TaskManager()

# Добавляем несколько задач
task_manager.add_task()
task_manager.add_task()

# Показываем все задачи
task_manager.show_tasks()

# Отмечаем задачу как выполненную
task_manager.task_completed()

# Показываем обновленный список задач
task_manager.show_tasks()

