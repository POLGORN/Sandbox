import sys
from parser import Format1Parser, Format2Parser, Format3Parser
from xlsx_writer import XlsxWriter

class App:
    def __init__(self, parser1, parser2, parser3, writer):
        self.parser1 = parser1
        self.parser2 = parser2
        self.parser3 = parser3
        self.writer = writer

    def load_text(self, path: str) -> str:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
        
    def run(self, in1_path, in2_path, in3_path, out_xlsx):
        t1 = self.load_text(in1_path)
        t2 = self.load_text(in2_path)
        t3 = self.load_text(in3_path)

        d1 = self.parser1.parse(t1)
        d2 = self.parser2.parse(t2)
        d3 = self.parser3.parse(t3)

        self.writer.filename = out_xlsx
        self.writer.write_sheet("Format1", d1)
        self.writer.write_sheet("Format2", d2)
        self.writer.write_sheet("Format3", d3)
        self.writer.save()

def main(argv):
    if len(argv) != 5:
        print("Usage: python app.py input1.txt input2.txt input3.txt output.xlsx")
        return 1
    _, in1, in2, in3, out = argv
    app = App(Format1Parser(), Format2Parser(), Format3Parser(), XlsxWriter(out))
    app.run(in1, in2, in3, out)
    print("Saved", out)
    return 0

if __name__ == '__main__':
    raise SystemExit(main(sys.argv))