import xml.etree.ElementTree as ET
import re

def extract_data_recursive(elem, extracted_data):
    if elem.text:
        matches = re.findall(r'!(.*?)~', elem.text)
        extracted_data.extend(matches)

    for attr in elem.attrib.values():
        matches = re.findall(r'!(.*?)~', attr)
        extracted_data.extend(matches)

    for child in elem:
        extract_data_recursive(child, extracted_data)

def main(xml_file, output_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    extracted_data = []

    extract_data_recursive(root, extracted_data)

    # Убираем дубликаты, сохраняя порядок
    unique_data = list(dict.fromkeys(extracted_data))

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(', '.join(unique_data))

    print(f"Данные записаны в {output_file}")

xml_file = 'z/input/input.xml'
output_file = 'z/output/output1.txt'

main(xml_file, output_file)