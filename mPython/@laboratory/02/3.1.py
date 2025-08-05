import xml.etree.ElementTree as ET
import os

# Определение путей к файлам
input_file_path = '@laboratory/input/input.xml'
output_file_path = '@laboratory/output/output3.1.txt'

# Проверка существования выходной директории
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

# Функция для удаления пространств имен
def remove_namespace(tag):
    return tag.split('}')[-1] if '}' in tag else tag

# Функция для форматирования XML с отступами
def format_xml(elem, indent=""):
    # Удаление пространств имен
    elem.tag = remove_namespace(elem.tag)
    result = f"{indent}<{elem.tag} { ' '.join([f'{k}=\"{v}\"' for k, v in elem.attrib.items()])}>"

    if len(elem):
        result += "\n"
        for child in elem:
            result += format_xml(child, indent + "  ")
        result += f"{indent}</{elem.tag}>\n"
    else:
        result += "/>\n"

    return result

# Загрузка XML
try:
    tree = ET.parse(input_file_path)
    root = tree.getroot()

    # Открытие выходного файла для записи
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        # Список для хранения элементов в нужной последовательности
        elements_to_write = []

        # Поиск нужных элементов и добавление в список
        elements_to_write.extend(root.findall('.//{http://www.plcopen.org/xml/tc6_0200}vendorElement'))
        elements_to_write.extend(root.findall('.//{http://www.plcopen.org/xml/tc6_0200}inVariable'))
        elements_to_write.extend(root.findall('.//{http://www.plcopen.org/xml/tc6_0200}connector'))
        elements_to_write.extend(root.findall('.//{http://www.plcopen.org/xml/tc6_0200}block'))
        elements_to_write.extend(root.findall('.//{http://www.plcopen.org/xml/tc6_0200}outVariable'))

        # Запись элементов в файл в нужной последовательности с 16 пробелами перед каждой строкой
        for elem in elements_to_write:
            formatted_xml = format_xml(elem)
            # Добавление 16 пробелов перед каждой строкой
            indented_lines = "\n".join([" " * 16 + line for line in formatted_xml.splitlines()])
            output_file.write(indented_lines)

    print(f"Данные успешно извлечены в {output_file_path}")

except FileNotFoundError:
    print(f"Файл {input_file_path} не найден.")
except ET.ParseError:
    print("Ошибка при парсинге XML файла.")
except Exception as e:
    print(f"Произошла ошибка: {e}")