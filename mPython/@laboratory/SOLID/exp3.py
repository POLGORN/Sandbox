"""
Программа фильтрует таблицу оставляя нужные строки
"""
import openpyxl
from abc import ABC, abstractmethod

# Интерфейс для модели
class IXLSXModel(ABC):
    @abstractmethod
    def get_columns(self):
        pass

    @abstractmethod
    def filter_data(self, column_name, value):
        pass

# Реализация модели
class XLSXModel(IXLSXModel):
    def __init__(self, file_path):
        self.file_path = file_path
        self.workbook = openpyxl.load_workbook(file_path)
        self.sheet = self.workbook.active

    def get_columns(self):
        return [cell.value for cell in self.sheet[1]]  # Получаем заголовки столбцов

    def filter_data(self, column_name, value):
        filtered_data = []
        header = self.get_columns()
        if column_name not in header:
            return filtered_data  # Если столбец не найден, возвращаем пустой список

        index = header.index(column_name)  # Находим индекс столбца
        filtered_data.append(header)  # Добавляем заголовки

        for row in self.sheet.iter_rows(min_row=2, values_only=True):
            cell_value = row[index]
            if cell_value is not None:
                # Приводим значения к строковому типу для сравнения
                if str(cell_value).strip() == str(value).strip():
                    filtered_data.append(row)

        return filtered_data

# Интерфейс для представления
class IXLSXView(ABC):
    @abstractmethod
    def display_columns(self, columns):
        pass

    @abstractmethod
    def display_results(self, filtered_data):
        pass

# Реализация представления
class XLSXView(IXLSXView):
    def display_columns(self, columns):
        print("Доступные столбцы:")
        for index, column in enumerate(columns):
            print(f"{index + 1}. {column}")

    def display_results(self, filtered_data):
        if filtered_data:
            for row in filtered_data:
                print(row)
        else:
            print("Данные не найдены.")

# Интерфейс для контроллера
class IXLSXController(ABC):
    @abstractmethod
    def run(self):
        pass

# Реализация контроллера
class XLSXController(IXLSXController):
    def __init__(self, model: IXLSXModel, view: IXLSXView):
        self.model = model
        self.view = view

    def run(self):
        columns = self.model.get_columns()
        self.view.display_columns(columns)

        column_index = int(input("Выберите номер столбца для фильтрации: ")) - 1
        column_name = columns[column_index]

        value = input(f"Введите значение для фильтрации в столбце '{column_name}': ")
        filtered_data = self.model.filter_data(column_name, value)
        self.view.display_results(filtered_data)

# Основная программа
if __name__ == "__main__":
    file_path = "input/data.xlsx"  # Укажите путь к вашему файлу XLSX

    model = XLSXModel(file_path)
    view = XLSXView()
    controller = XLSXController(model, view)

    controller.run()
