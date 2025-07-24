import unittest
from unittest.mock import patch
import tkinter as tk
from view import View

class TestView(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.view = View(self.root)

    @patch('view.messagebox.showinfo')  # Замокируем метод showinfo
    def test_show_message(self, mock_showinfo):
        # Действие
        self.view.show_message("Тестовое сообщение")

        # Проверка
        mock_showinfo.assert_called_once_with("Информация", "Тестовое сообщение")

if __name__ == "__main__":
    unittest.main()
"""
Объяснение изменений
Импорт patch: Мы импортируем patch из unittest.mock, чтобы замокировать метод showinfo из messagebox.
Замокирование showinfo: Мы используем декоратор @patch('view.messagebox.showinfo'), чтобы замокировать метод showinfo перед его вызовом в тесте. Это позволяет нам проверить, был ли он вызван с правильными аргументами.
Проверка вызова: Мы проверяем, что mock_showinfo был вызван с ожидаемыми аргументами.
"""
# ___________________________________________________________________
# import unittest  # Импортируем модуль unittest для написания тестов
# from unittest.mock import patch  # Импортируем patch для замены объектов в тестах
# import tkinter as tk  # Импортируем библиотеку tkinter для создания графического интерфейса
# from view import View  # Импортируем класс View из модуля view

# class TestView(unittest.TestCase):
#     # Метод, который выполняется перед каждым тестом
#     def setUp(self):
#         self.root = tk.Tk()  # Создаем корневое окно для тестирования
#         self.view = View(self.root)  # Создаем экземпляр представления

#     @patch('view.messagebox.showinfo')  # Замокируем метод showinfo из messagebox
#     def test_show_message(self, mock_showinfo):
#         # Действие
#         self.view.show_message("Тестовое сообщение")  # Вызываем метод show_message с тестовым сообщением

#         # Проверка
#         mock_showinfo.assert_called_once_with("Информация", "Тестовое сообщение")  # Проверяем, что showinfo был вызван с правильными аргументами

# # Проверяем, является ли этот файл основным модулем
# if __name__ == "__main__":
#     unittest.main()  # Запускаем все тесты
"""
___________________________________________________________________
<<< Порядок работы программы >>>

    Импорт библиотек:
        Программа начинает с импорта модуля unittest, который используется для написания и выполнения тестов, а также patch из unittest.mock для замены объектов в тестах. Импортируется библиотека tkinter для создания графического интерфейса и класс View из модуля view, который будет тестироваться.
    Определение класса TestView:
        Создается класс TestView, который наследует от unittest.TestCase. Этот класс будет содержать тесты для представления.
    Метод setUp:
        Метод setUp вызывается перед каждым тестом. В этом методе создается корневое окно self.root и экземпляр View, который будет использоваться в тестах. Это позволяет обеспечить чистое состояние для каждого теста.
    Тестирование метода show_message:
        Метод test_show_message проверяет, что метод show_message вызывает messagebox.showinfo с правильными аргументами.
        Замокировка:
            Декоратор @patch('view.messagebox.showinfo') замокирует метод showinfo, чтобы предотвратить его фактический вызов и вместо этого создать поддельный объект mock_showinfo.
        Действие:
            Вызывается метод show_message с тестовым сообщением "Тестовое сообщение".
        Проверка:
            С помощью assert_called_once_with проверяется, что замокированный метод showinfo был вызван один раз с аргументами "Информация" и "Тестовое сообщение".
    Запуск тестов:
        В блоке if __name__ == "__main__": программа проверяет, запущен ли этот файл как основной модуль. Если да, то вызывается unittest.main(), который запускает все тесты, определенные в классе TestView.
"""