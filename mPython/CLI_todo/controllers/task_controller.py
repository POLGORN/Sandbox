# Контроллер
# Управляет задачами добавляет удаляет и обновляет их
#---------------------------------------------------------
from models.task import Task

class TaskController:
    def __init__(self):
        # Инициализация контроллера задач с пустым списком 
        self.tasks = []
    
    def add_task(self, title, description=""):
        # Метод для добавления новой задачи в список
        task = Task(title, description)
        self.tasks.append(task)

    def remove_task(self, index):
        # Метод для удаления задачи по индексу если он валиден
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        
    def complete_task(self, index):
        # Метод для пометки задачи как выполненной по индексу
        if 0 <=  index < len(self.tasks):
            self.tasks[index].is_completed = True

    def update_task(self, index, title=None, description=None):
        # Метод для обновления заголовка и/или описания задачи по индексу
        if 0 <= index < len(self.tasks):
            if title is not None:
                self.tasks[index].title = title
            if description is not None:
                self.tasks[index].description = description

    def get_tasks(self):
        # Метод для получения списка всех задач
        return self.tasks
