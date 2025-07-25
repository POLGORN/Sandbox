from view import View # Импортируем представление
from model import Model # Импортируем модель

class Controller:
    def __init__(self, root):
        # Метод инициализации
        self.model = Model() # Создаем экземпляр модели
        self.view = View(root) # Создаем экземпляр представления
        self.view.set_button_command(self.on_button_click) # Задаем команду для кнопки "Нажми меня"

    def on_button_click(self):
        # Метод действия при нажатии на кнопку
        user_input = self.view.get_input() # Получаем данные пользователя из поля
        self.model.set_message(user_input) # Записываем новые данные в модель
        message = self.model.get_message() # Получаем данные из модели
        self.view.show_message(message)    # Выводим сообщение в всплывающее окно