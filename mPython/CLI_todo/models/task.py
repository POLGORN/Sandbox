# Модель
# Определяет класс Task которы представляет задачу
#---------------------------------------------------
class Task:
    def __init__(self, title, description=""):
        # Инициализация задачи с заголовком и описанием
        self.title = title
        self.description = description
        # Атрибут для отслеживания статуса выполнения задачи
        self.is_completed = False

    def __str__(self):
        # Метод для отображения задачи в строковм формате
        # Использует символ "V" для выполненной задачи и "Х" для невыполненной
        status = "V" if self.is_completed else "X"
        return f"[{status}] {self.title} {self.description}"
