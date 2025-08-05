import xml.etree.ElementTree as ET
import re
import logging
import pandas as pd

class DataSourceExtractor:
    """Абстрактный класс для извлечения данных из источников"""
    def extract(self):
        # Метод для извлечения данных, должен быть переопределен в подклассах
        raise NotImplementedError("Метод extract должен быть переопределен.")

class XmlFileExtractor(DataSourceExtractor):
    """Класс для извлечения данных из XML файла"""
    def __init__(self, xml_file_path):
        # Инициализация с указанием XML файла
        self.xml_file_path = xml_file_path
        self.extracted_items = []  # Список для хранения извлеченных данных

    def _recursive_extract(self, element):
        # Рекурсивный метод для извлечения данных из XML элемента
        if element.text:
            # Ищем совпадения в тексте элемента
            matches = re.findall(r'!(.*?)~', element.text)
            self.extracted_items.extend(matches)  # Добавляем найденные данные

        # Ищем совпадения в атрибутах элемента
        for attribute in element.attrib.values():
            matches = re.findall(r'!(.*?)~', attribute)
            self.extracted_items.extend(matches)

        # Рекурсивно обрабатываем дочерние элементы
        for child in element:
            self._recursive_extract(child)

    def extract(self):
        # Метод для извлечения данных из XML файла
        try:
            tree = ET.parse(self.xml_file_path)  # Парсим XML файл
        except FileNotFoundError:
            logging.error(f"Ошибка: Файл {self.xml_file_path} не найден.")
            return []
        except ET.ParseError:
            logging.error(f"Ошибка: Файл {self.xml_file_path} не является корректным XML.")
            return []

        root = tree.getroot()  # Получаем корневой элемент
        self._recursive_extract(root)  # Запускаем рекурсивное извлечение
        unique_items = list(dict.fromkeys(self.extracted_items))  # Удаляем дубликаты
        logging.info("Извлечение данных завершено.")
        return unique_items  # Возвращаем уникальные данные

class ExcelDataReader:
    """Класс для загрузки данных из Excel файла"""
    @staticmethod
    def read(file_path):
        # Статический метод для загрузки данных из указанного Excel файла
        return pd.read_excel(file_path)  # Возвращаем DataFrame с загруженными данными

class DataProcessor:
    """Класс для обработки и фильтрации данных"""
    def __init__(self, data):
        # Инициализация с данными для обработки
        self.data = data

    def _apply_filters(self, df, filters):
        # Метод для фильтрации данных по заданным фильтрам
        for column, values in filters.items():
            df = df[df[column].isin(values)]  # Фильтруем DataFrame по каждому столбцу
        return df

    def _get_user_filters(self, df):
        # Метод для получения фильтров от пользователя
        filters = {}
        logging.info("Доступные столбцы: %s", df.columns.tolist())
        while True:
            column = input("Введите имя столбца для фильтрации (или 'exit' для выхода): ")
            if column.lower() == 'exit':
                break  # Выход из цикла
            if column not in df.columns:
                logging.warning("Этот столбец не существует. Пожалуйста, попробуйте снова.")
                continue  # Запрашиваем имя столбца снова
            values = input(f"Введите значения для фильтрации в столбце '{column}' (через запятую): ")
            values_list = [value.strip() for value in values.split(',')]  # Разделяем значения
            filters[column] = values_list  # Сохраняем фильтры
        return filters

    def save_to_file(self, df, output_file):
        # Метод для сохранения DataFrame в текстовый файл
        df.to_csv(output_file, sep='\t', index=False)  # Сохраняем в формате TSV

    def process_data(self):
        # Метод для обработки данных
        df = pd.DataFrame(self.data, columns=['Extracted Data'])  # Создаем DataFrame из извлеченных данных

        if len(df.columns) > 1:
            filters = self._get_user_filters(df)  # Получаем фильтры от пользователя
            filtered_data = self._apply_filters(df, filters)  # Фильтруем данные
        else:
            filtered_data = df  # Если только один столбец, не фильтруем

        logging.info("Отфильтрованные данные: ")
        logging.info("%s", filtered_data)  # Логируем отфильтрованные данные

        output_file = 'output/output.txt'  # Имя выходного файла
        self.save_to_file(filtered_data, output_file)  # Сохраняем отфильтрованные данные
        logging.info("Отфильтрованные данные сохранены в '%s'.", output_file)  # Логируем успешное сохранение