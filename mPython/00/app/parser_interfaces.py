from abc import ABC, abstractmethod
from typing import Dict, List

class IParser(ABC):
    @abstractmethod
    def parse(self, text: str) -> Dict[str, List[str]]:
        """Парсит текст и возвращает словарь column_name -> list_of_values"""
        ...