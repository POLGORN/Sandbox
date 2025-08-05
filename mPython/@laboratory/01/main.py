import logging
from DataManager import XmlFileExtractor, DataProcessor, ExcelDataReader

def main():
    logging.basicConfig(level=logging.INFO)

    # Извлечение данных из XML
    xml_file_path = 'input/input.xml'
    xml_extractor = XmlFileExtractor(xml_file_path)
    extracted_data = xml_extractor.extract()

    if extracted_data:
        data_processor = DataProcessor(extracted_data)
        data_processor.process_data()

    # Загрузка данных из Excel
    excel_file_path = 'input/data.xlsx'
    excel_data = ExcelDataReader.read(excel_file_path)

    # Получение фильтров от пользователя только для Excel данных
    filters = data_processor._get_user_filters(excel_data)  # Запрашиваем фильтры только для данных из Excel

    # Фильтрация данных
    filtered_data_excel = data_processor._apply_filters(excel_data, filters)

    # Вывод отфильтрованных данных
    logging.info("Отфильтрованные данные из Excel:")
    logging.info("%s", filtered_data_excel)

    # Сохранение отфильтрованных данных в .txt файл
    output_file_path = 'output/output2.txt'
    data_processor.save_to_file(filtered_data_excel, output_file_path)
    logging.info("Отфильтрованные данные сохранены в '%s'.", output_file_path)

if __name__ == "__main__":
    main()