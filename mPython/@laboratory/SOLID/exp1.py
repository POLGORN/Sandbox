"""
Программа находит данные с маркерами !_~
"""
import xml.etree.ElementTree as ET
import re
from abc import ABC, abstractmethod

# Интерфейс для модели
class IXMLModel(ABC):
    @abstractmethod
    def find_data(self):
        pass

# Реализация модели
class XMLModel(IXMLModel):
    def __init__(self, xml_data):
        self.root = ET.fromstring(xml_data)

    def find_data(self):
        results = set()  # Используем множество для хранения уникальных значений
        for elem in self.root.iter():
            if elem.text:
                results.update(self.extract_data(elem.text))
            for attr in elem.attrib.values():
                results.update(self.extract_data(attr))
        return list(results)

    def extract_data(self, text):
        pattern = r'!(.*?)~'
        return re.findall(pattern, text)

# Интерфейс для представления
class IXMLView(ABC):
    @abstractmethod
    def display_results(self, results):
        pass

# Реализация представления
class XMLView(IXMLView):
    def display_results(self, results):
        if results:
            print("Найденные данные:")
            for result in results:
                print(result)
        else:
            print("Данные не найдены.")

# Контроллер
class XMLController:
    def __init__(self, model: IXMLModel, view: IXMLView):
        self.model = model
        self.view = view

    def process_data(self):
        results = self.model.find_data()
        self.view.display_results(results)

# Основная программа
if __name__ == "__main__":
    xml_data = """
    <root>
        <item attr="!data1~">Some text !data2~ more text</item>
        <item attr="!data3~">Another text</item>
            <item attr="!data3~">!Another text~</item>
        <item attr="!data3~">Another text</item>
    </root>
    """
    
    model = XMLModel(xml_data)
    view = XMLView()
    controller = XMLController(model, view)
    
    controller.process_data()
