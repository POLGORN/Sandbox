class DataReaderFactory:
    @staticmethod
    def create_reader(file_type):
        if file_type == 'xml':
            return XmlReader()
        elif file_type == 'xlsx':
            return XlsxReader()
        else:
            raise ValueError("Неподдерживаемый формат файла")
# _____________________________________________________________

class DataReaderFactory:
    readers = {
        'xml': XmlReader,
        'xlsx': XlsxReader
    } 

    @staticmethod
    def create_reader(file_type):
        if file_type in DataReaderFactory.readers:
            return DataReaderFactory.readers[file_type]()
        else:
            raise ValueError("Неподдерживаемый формат")
# _____________________________________________________________

if __name__ == "__main__":
  # ...
  xml_reader = DataReaderFactory.create_reader('xml')
  xlsx_reader = DataReaderFactory.create_reader('xlsx')
  # ...
