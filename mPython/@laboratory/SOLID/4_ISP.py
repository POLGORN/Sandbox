# =======================================================
# Interface Segregation Principle
"""
Принцип разделения интерфейса утверждает что клиенты не должны
зависеть от интерфейсов которые они не используют 
Иначе говоря лучше иметь несколько специализированных интерфейсов 
чем один универсальный
...
Интерфейсы должны быть специфичными и не перегруженными
"""
class Printable:
    def print(self):
        pass

class Sendable:
    def send(self):
        pass

class PDFReport(Printable, Sendable):
    def print(self):
        # Логика печати PDF отчёта
        pass

    def send(self):
        # Логика отправки PDF отчёта
        pass
# =======================================================
""" НЕ ПРАВИЛЬНО """
class Document:
    def open_document(self):
        pass

    def save_document(self):
        pass

    def close_document(self):
        pass

class DocumentEditor(Document):
    def open_document(self):
        # Код который открывает документ

    def save_document(self):
        # Код который сохраняет документ

    def close_docuument(self):
        # Код который открывает документ
# =======================================================
""" ПРАВИЛЬНО """
class OpenDocument:
    def open_document(self):
        pass

class SaveDocument:
    def save_document(self):
        pass

class CloseDocument:
    def close_document(self):
        pass

class FirstDocumentEditor(OpenDocument, CloseDocument):
    def open_document(self):
        # Код который открывает документ

    def close_document(self):
        # Код который закрывает документ

class SecondDocumentEditor(SaveDocument, CloseDocument):
    def save_document(self):
        # Код который сохраняет документ

    def close_document(self):
        # Код который закрывает документ
# =======================================================
""" ТАК ТОЖЕ ПРАВИЛЬНО """
class Document: # <--- Это интерфейс
    def open_document(self):
        raise NotImplementedError("Subclasses should implement this method")

class Savable: # <--- Это интерфейс
    def save_document(self):
        raise NotImplementedError("Subclasses should implement this method")

class Closable: # <--- Это интерфейс
    def close_document(self):
        raise NotImplementedError("Subclasses should implement this method")

class FirstDocumentEditor(Document, Savable):
    def open_document(self):
        # Код который открывает документ
        print("Документ открыт")

    def save_document(self):
        # Код который сохраняет документ
        print("Документ сохранён")

class SecornDocumentEditor(Document, Closable):
    def open_document(self):
        # Код который открывает документ
        print("Документ открыт")

    def close_document(self):
        # Код который закрывает документ
        print("Документ закрыт")
# =======================================================