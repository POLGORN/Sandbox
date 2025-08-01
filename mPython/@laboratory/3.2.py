import xml.etree.ElementTree as ET
import os
import pandas as pd

# Определение путей к файлам
input_file_path = '@laboratory/input/input.xml'
output_file_path = '@laboratory/output/outputX1.txt'
output_data_path = '@laboratory/input/input.txt'  # Путь к файлу с данными
output_columns_path = '@laboratory/output/output1.txt'  # Путь к файлу с названиями столбцов

# Проверка существования выходной директории
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

# Функция для удаления пространств имен
def remove_namespace(tag):
    return tag.split('}')[-1] if '}' in tag else tag

# Функция для форматирования XML с отступами
def format_xml(elem, indent=""):
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

# Функция для замены значений в шаблоне XML
def replace_values(template, row):
    for col in columns:
        if col in row:
            placeholder = f"!{col}~"
            template = template.replace(placeholder, str(row[col]))
    return template

# Загрузка данных и названий столбцов
with open(output_columns_path, 'r', encoding='utf-8') as f:
    columns = f.read().strip().split(', ')

data = pd.read_csv(output_data_path, delimiter='\t')

# Загрузка XML шаблона
with open(input_file_path, 'r', encoding='utf-8') as f:
    xml_template = f.read()

# Начало общего XML
output_xml = '<?xml version="1.0" encoding="utf-8"?>\n<project xmlns="http://www.plcopen.org/xml/tc6_0200">\n'
output_xml += '  <fileHeader companyName="Prosoft-Systems Ltd." productName="Astra.IDE" productVersion="Astra.IDE_V1.7.2.1" creationDateTime="2025-07-24T10:35:59.4336606" />\n'
output_xml += '  <contentHeader name="AKS_v2.project" modificationDateTime="2025-07-24T08:15:04.4598718">\n'
output_xml += '    <coordinateInfo>\n      <fbd>\n        <scaling x="1" y="1" />\n      </fbd>\n      <ld>\n        <scaling x="1" y="1" />\n      </ld>\n      <sfc>\n        <scaling x="1" y="1" />\n      </sfc>\n    </coordinateInfo>\n'
output_xml += '    <addData>\n      <data name="http://www.3s-software.com/plcopenxml/projectinformation" handleUnknown="implementation">\n        <ProjectInformation />\n      </data>\n    </addData>\n  </contentHeader>\n'
output_xml += '  <types>\n    <dataTypes />\n    <pous>\n'

# Генерация XML для каждой строки данных
for index, row in data.iterrows():
    filled_xml = replace_values(xml_template, row)
    # Извлечение содержимого между <CFC> и </CFC>
    start_index = filled_xml.find('<CFC')
    end_index = filled_xml.find('</CFC>') + len('</CFC>')
    cfc_content = filled_xml[start_index:end_index]
    
    # Добавление содержимого в общий XML
    output_xml += '      ' + cfc_content + '\n'

output_xml += '    </pous>\n  </types>\n  <instances>\n    <configurations />\n  </instances>\n  <addData>\n    <data name="http://www.3s-software.com/plcopenxml/projectstructure" handleUnknown="discard">\n      <ProjectStructure>\n      <Folder Name="test">\n          <Folder Name="Blank">\n            <Object Name="AI__1_1" ObjectId="4da1f976-cd55-4be1-9507-1d52be8220e5" />\n          </Folder>\n        </Folder>\n      </ProjectStructure>\n    </data>\n  </addData>\n</project>'

# Запись общего XML в файл
with open('@laboratory/output/output3.2.xml', 'w', encoding='utf-8') as f:
    f.write(output_xml)

print("XML файл успешно создан.")