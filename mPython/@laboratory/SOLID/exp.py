import xml.etree.ElementTree as ET
import re

class XMLModel:
    def __init__(self, xml_data):
        self.root = ET.fromstring(xml_data)

    def find_data(self):
        results = set()  # Используем множество для хранения уникальных значений
        for elem in self.root.iter():
            # Проверка значений элементов
            if elem.text:
                results.update(self.extract_data(elem.text))
            # Проверка атрибутов элементов
            for attr in elem.attrib.values():
                results.update(self.extract_data(attr))
        return list(results)  # Преобразуем множество обратно в список

    def extract_data(self, text):
        # Используем регулярное выражение для поиска данных между '!' и '~'
        pattern = r'!(.*?)~'
        return re.findall(pattern, text)


class XMLView:
    def display_results(self, results):
        if results:
            print("Найденные данные:")
            for result in results:
                print(result)
        else:
            print("Данные не найдены.")


class XMLController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def process_data(self):
        results = self.model.find_data()
        self.view.display_results(results)


if __name__ == "__main__":
    xml_data = """
    <root>
        <item attr="!data1~">Some text !data2~ more text</item>
        <item attr="!data3~">Another text</item>
        <item attr="!data3~">Another text</item>
        <item attr="!data3~">Another text</item>
    </root>
    """
    
    model = XMLModel(xml_data)
    view = XMLView()
    controller = XMLController(model, view)
    
    controller.process_data()
