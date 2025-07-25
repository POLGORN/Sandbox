import unittest # Импортируем библиотеку для тестов
from model import Model # Импортируем модуль для теста

class TestModel(unittest.TestCase):
    def setUp(self):
        # Метод инициализация
        self.model = Model() # Создаем экземпляр класса

    def test_get_message(self):
        # Метод проверки получения базового сообщения
        self.assertEqual(self.model.get_message(), "Это пустышка")

    def test_set_message(self):
        # Метод проверки получение нового сообщения
        new_message = "Новое сообщение"
        self.model.set_message(new_message)
        self.assertEqual(self.model.get_message(), new_message)

if __name__ == "__main__":
    # Тест запускается только напрямую
    unittest.main()