import unittest # Импортируем библиотеку для тестов
from unittest.mock import MagicMock # Импортируем усиленные заглушки
from controller import Controller # Импортируем модель для теста

class TestController(unittest.TestCase):
    def setUp(self):
        self.controller = Controller(MagicMock())
        # Создаем экземпляр контроллера с поддельным обьектом для представления

    def test_on_button_click_updates_model_and_view(self):
        # Метод тестирования буквально всего приложения
        self.controller.view.get_input = MagicMock(return_value="Тестовое сообщение") # Проверяем метод получение данных через поле ввода
        self.controller.view.show_message = MagicMock() # Создаем поддельный метод
        
        self.controller.on_button_click() # Проверяем метод нажатия на кнопку в контроллере

        self.assertEqual(self.controller.model.get_message(), "Тестовое сообщение") # Проверяем обновляется ли сообщение в модели
        self.controller.view.show_message.assert_called_once_with("Тестовое сообщение") # Проверяем всплывающее окно

if __name__ == "__main__":
    # Тест запускается только напрямую
    unittest.main()