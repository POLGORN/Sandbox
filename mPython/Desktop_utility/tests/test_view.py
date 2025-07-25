import unittest # Импортируем библиотеку для тестов
import tkinter as tk # Импортируем билиотеку для GUI
from unittest.mock import patch # Импортируем заглушки
from view import View # Импортируем наш модуль для теста

class TestView(unittest.TestCase):
    def setUp(self):
        # Метод инициализации
        self.root = tk.Tk() # Создаем корневое окно
        self.view = View(self.root) 
        # Создаем экземпляр представления передавая в корневое окно

    @patch('view.messagebox.showinfo') # Замокируем метод showinfo
    def test_show_message(self, mock_showinfo):
        # Проверка метода show_message
        self.view.show_message("Тестовое сообщение")

        # Проверяем что showinfo вызван с правильными аргументами
        mock_showinfo.assert_called_once_with("Информация", "Тестовое сообщение")

if __name__ == "__maim__":
    # Тест запускается только напрямую
    unittest.main()