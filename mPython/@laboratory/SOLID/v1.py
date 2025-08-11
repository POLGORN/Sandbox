import xml.etree.ElementTree as ET

# Model
class XmlElement:
    def __init__(self, tag, attributes, text):
        self.tag = tag
        self.attributes = attributes
        self.text = text

# Service
class XmlReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        tree = ET.parse(self.file_path)
        root = tree.getroot()
        elements = []

        for child in root:
            element = XmlElement(child.tag, child.attrib, child.text)
            elements.append(element)

        return elements

# View
class XmlView:
    @staticmethod
    def display_element(element):
        print(f"Тег: {element.tag}, Атрибуты: {element.attributes}, Значение: {element.text}")

    @staticmethod
    def display_elements(elements):
        for element in elements:
            XmlView.display_element(element)

# Main application
if __name__ == "__main__":
    file_path = "example.xml"  # Укажите путь к вашему XML-файлу
    reader = XmlReader(file_path)
    view = XmlView()

    # Чтение и отображение элементов XML
    elements = reader.read()
    view.display_elements(elements)
