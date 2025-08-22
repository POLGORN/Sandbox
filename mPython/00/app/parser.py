import re
from typing import Dict, List
from parser_interfaces import IParser

class Format1Parser(IParser):
    def parse(self, text: str) -> Dict[str, List[str]]:
        data = {}
        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            m = re.match(r'^([^:]+)\s*:\s*(.+)$', line)
            if not m:
                continue
            key = m.group(1).strip()
            vals = [v.strip() for v in m.group(2).split(',') if v.strip() != '']
            data[key] = vals
        return data

class Format2Parser(IParser):
    def parse(self, text: str) -> Dict[str, List[str]]:
        lines = [l.strip() for l in text.splitlines() if l.strip() != '']
        if not lines:
            return {}
        rows = [ [c.strip() for c in line.split(',')] for line in lines ]
        headers = rows[0]
        cols = {h: [] for h in headers}
        for row in rows[1:]:
            while len(row) < len(headers):
                row.append('')
            for i, h in enumerate(headers):
                cols[h].append(row[i])
        return cols

class Format3Parser(IParser):
    def parse(self, text: str) -> Dict[str, List[str]]:
        lines = [l.strip() for l in text.splitlines() if l.strip() != '']
        if len(lines) < 2:
            return {}
        def split_row(line: str):
            return [p.strip() for p in line.strip('|').split('|')]
        headers = split_row(lines[0])
        data_rows = []
        for line in lines[2:]:
            data_rows.append(split_row(line))
        cols = {h: [] for h in headers}
        for row in data_rows:
            while len(row) < len(headers):
                row.append('')
            for i, h in enumerate(headers):
                cols[h].append(row[i])
        return cols