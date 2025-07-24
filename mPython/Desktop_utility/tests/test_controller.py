import unittest
from unittest.mock import MagicMock
from controller import Controller

class TestController(unittest.TestCase):
    def setUp(self):
        self.controller = Controller(MagicMock())

    def test_on_button_click_updates_model_and_view(self):
        self.controller.view.get_input = MagicMock(return_value="Тестовое сообщение")
        self.controller.view.show_message = MagicMock()

        self.controller.on_button_click()

        self.assertEqual(self.controller.model.get_message(), "Тестовое сообщение")
        self.controller.view.show_message.assert_called_once_with("Тестовое сообщение")

if __name__ == "__main__":
    unittest.main()
# _____________________________________________________________________________________
# import unittest  # Импортируем модуль unittest для написания тестов
# from unittest.mock import MagicMock  # Импортируем MagicMock для создания поддельных объектов
# from controller import Controller  # Импортируем класс Controller из модуля controller

# class TestController(unittest.TestCase):
#     # Метод, который выполняется перед каждым тестом
#     def setUp(self):
#         self.controller = Controller(MagicMock())  # Создаем экземпляр контроллера с поддельным объектом для представления

#     # Тестируем метод on_button_click
#     def test_on_button_click_updates_model_and_view(self):
#         # Подготовка
#         self.controller.view.get_input = MagicMock(return_value="Тестовое сообщение")  # Настраиваем метод get_input для возврата тестового сообщения
#         self.controller.view.show_message = MagicMock()  # Создаем поддельный метод show_message

#         # Действие
#         self.controller.on_button_click()  # Вызываем метод on_button_click контроллера

#         # Проверка
#         self.assertEqual(self.controller.model.get_message(), "Тестовое сообщение")  # Проверяем, что сообщение в модели обновлено
#         self.controller.view.show_message.assert_called_once_with("Тестовое сообщение")  # Проверяем, что show_message был вызван с правильным аргументом

# # Проверяем, является ли этот файл основным модулем
# if __name__ == "__main__":
#     unittest.main()  # Запускаем все тесты
"""
_____________________________________________________________________________________
<<< Порядок работы программы >>>

    Импорт библиотек:
        Программа начинает с импорта модуля unittest, который используется для написания и выполнения тестов, а также MagicMock из unittest.mock для создания поддельных объектов, которые имитируют поведение реальных объектов.
    Определение класса TestController:
        Создается класс TestController, который наследует от unittest.TestCase. Этот класс будет содержать тесты для контроллера.
    Метод setUp:
        Метод setUp вызывается перед каждым тестом. В этом методе создается новый экземпляр Controller, передавая поддельный объект (созданный с помощью MagicMock) в качестве представления. Это позволяет изолировать тесты от реального интерфейса.
    Тестирование метода on_button_click:
        Метод test_on_button_click_updates_model_and_view проверяет, что метод on_button_click контроллера корректно обновляет модель и вызывает метод представления для отображения сообщения.
        Подготовка:
            Метод get_input представления настраивается с помощью MagicMock, чтобы он возвращал тестовое сообщение "Тестовое сообщение".
            Метод show_message также заменяется на поддельный метод, чтобы отслеживать его вызовы.
        Действие:
            Вызывается метод on_button_click, который должен обновить модель и вызвать метод show_message.
        Проверка:
            С помощью assertEqual проверяется, что сообщение в модели обновлено до "Тестовое сообщение".
            С помощью assert_called_once_with проверяется, что метод show_message был вызван один раз с правильным аргументом.
    Запуск тестов:
        В блоке if __name__ == "__main__": программа проверяет, запущен ли этот файл как основной модуль. Если да, то вызывается unittest.main(), который запускает все тесты, определенные в классе TestController.
"""