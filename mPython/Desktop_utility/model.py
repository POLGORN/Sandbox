class Model:
    def __init__(self):
        self.message = "Эта кнопка пока ничего не делает!"

    def get_message(self):
        return self.message

    def set_message(self, new_message):
        self.message = new_message
# _____________________________________________
# class Model:
#     def __init__(self):
#         # Инициализация модели с сообщением по умолчанию
#         self.message = "Эта кнопка пока ничего не делает!"  # Устанавливаем текст сообщения

#     def get_message(self):
#         # Метод для получения текущего сообщения
#         return self.message  # Возвращаем текущее сообщение

#     def set_message(self, new_message):
#         # Метод для установки нового сообщения
#         self.message = new_message  # Обновляем значение атрибута message новым значением