class Model:
    def __init__(self):
        # Метод инициализации
        self.message = "Это пустышка"

    def get_message(self):
        # Метод получения базового сообщения
        return self.message

    def set_message(self, new_message):
        # Метод получения нового сообщения
        self.message = new_message