import xml.etree.ElementTree as ET

class XMLParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tree = self.load_xml()

    def load_xml(self):
        """Загружает и парсит XML из файла."""
        return ET.parse(self.file_path)

    def find_elements(self, tag_name):
        """Находит все элементы с заданным тегом."""
        root = self.tree.getroot()
        return root.findall('.//' + tag_name)

class XMLFormatter:
    @staticmethod
    def format_element(element, indent=0):
        """Форматирует элемент с отступами."""
        indent_str = '  ' * indent
        xml_str = ""

        # Добавляем атрибуты, если есть
        if element.attrib:
            attrs = ' '.join(f'{key}="{value}"' for key, value in element.attrib.items())
            xml_str += f"{indent_str}<{element.tag} {attrs}>\n"
        else:
            xml_str += f"{indent_str}<{element.tag}>\n"

        # Добавляем текстовое содержимое, если есть
        if element.text and element.text.strip():
            xml_str += f"{indent_str}  {element.text.strip()}\n"

        # Рекурсивно добавляем дочерние элементы
        for child in element:
            xml_str += XMLFormatter.format_element(child, indent + 1)

        # Добавляем текстовое содержимое после дочерних элементов, если есть
        if element.tail and element.tail.strip():
            xml_str += f"{indent_str}{element.tail.strip()}\n"

        xml_str += f"{indent_str}</{element.tag}>\n"  # Закрывающий тег
        return xml_str

    @staticmethod
    def format_element_without_tags(element):
        """Форматирует элемент без тегов, включая его содержимое."""
        xml_str = ""

        # Добавляем атрибуты, если есть
        if element.attrib:
            attrs = ' '.join(f'{key}="{value}"' for key, value in element.attrib.items())
            xml_str += f"<{element.tag} {attrs}>\n"
        else:
            xml_str += f"<{element.tag}>\n"

        # Добавляем текстовое содержимое, если есть
        if element.text and element.text.strip():
            xml_str += f"  {element.text.strip()}\n"

        # Рекурсивно добавляем дочерние элементы
        for child in element:
            xml_str += XMLFormatter.format_element_without_tags(child)

        # Закрываем элемент
        xml_str += f"</{element.tag}>\n"
        return xml_str

class XMLContentExtractor:
    def __init__(self, parser):
        self.parser = parser

    def extract_content(self, tag_name):
        """Извлекает содержимое элементов с заданным тегом без самих тегов."""
        elements = self.parser.find_elements(tag_name)
        content = ""
        for element in elements:
            # Извлекаем только дочерние элементы без родительского тега
            for child in element:
                content += XMLFormatter.format_element_without_tags(child)
        return content

# Пример использования
file_path = 'input/data.xml'  # Путь к вашему XML-файлу
parser = XMLParser(file_path)
extractor = XMLContentExtractor(parser)

# Извлекаем содержимое тегов без самих тегов
content = extractor.extract_content('new1')
print(content)

# Извлекаем содержимое тегов 'book' с тегами
for book in parser.find_elements('book'):
    formatted_xml = XMLFormatter.format_element(book)
    print(formatted_xml)