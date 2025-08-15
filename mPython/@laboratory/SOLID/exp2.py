"""
Программа фильтрует таблицу оставляя нужные столбцы
"""
import openpyxl
from abc import ABC, abstractmethod

# Интерфейс для модели
class IXLSXModel(ABC):
    @abstractmethod
    def filter_columns(self, columns_to_keep):
        pass

# Реализация модели
class XLSXModel(IXLSXModel):
    def __init__(self, file_path):
        self.file_path = file_path
        self.workbook = openpyxl.load_workbook(file_path)
        self.sheet = self.workbook.active

    def filter_columns(self, columns_to_keep):
        filtered_data = []
        header = [cell.value for cell in self.sheet[1]]  # Получаем заголовки столбцов
        indices_to_keep = [index for index, value in enumerate(header) if value in columns_to_keep]

        # Добавляем заголовки отфильтрованных столбцов
        filtered_data.append([header[index] for index in indices_to_keep])

        # Добавляем данные отфильтрованных столбцов
        for row in self.sheet.iter_rows(min_row=2, values_only=True):
            filtered_row = [row[index] for index in indices_to_keep]
            filtered_data.append(filtered_row)

        return filtered_data

# Интерфейс для представления
class IXLSXView(ABC):
    @abstractmethod
    def display_results(self, filtered_data):
        pass

# Реализация представления
class XLSXView(IXLSXView):
    def display_results(self, filtered_data):
        for row in filtered_data:
            print(row)

# Контроллер
class XLSXController:
    def __init__(self, model: IXLSXModel, view: IXLSXView):
        self.model = model
        self.view = view

    def process_data(self, columns_to_keep):
        filtered_data = self.model.filter_columns(columns_to_keep)
        self.view.display_results(filtered_data)

# Основная программа
if __name__ == "__main__":
    file_path = "input/data.xlsx"  # Укажите путь к вашему файлу XLSX
    columns_to_keep = {"title", "year"}  # Укажите столбцы, которые нужно оставить

    model = XLSXModel(file_path)
    view = XLSXView()
    controller = XLSXController(model, view)

    controller.process_data(columns_to_keep)
