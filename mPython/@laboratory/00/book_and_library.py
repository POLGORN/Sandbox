class Book: # У нас есть книга
    def __init__(self, title, author): # У неё самой есть два атрибута - название и автор
        self.title = title # Название
        self.author = author # Автор

    def __str__(self): # Строковое представление книги есть
        return f'"{self.title}" by {self.author}'

class Library: # Есть библиотека
    def __init__(self): # Без атрибутов
        self.books = [] # Но со списком книг (пока пустым)

    def add_book(self, book): # В библиотеку могут принести книги
        self.books.append(book) # Добавляем к СПИСКУ КНИГ САМОГО КЛАССА

    '''СОВЕРШЕННО НОВЫЙ ФУНКЦИОНАЛ'''
    def remove_book(self, title): # НО МОГУТ И ЗАБРАТЬ
        self.books = [book for book in self.books if book.title != title]

    def list_books(self): # Есть список всех книг библиотеки
        for book in self.books: # За каждую книгу в списке
            print(book) # Выведи её

    '''СОВЕРШЕННО НОВЫЙ ФУНКЦИОНАЛ'''
    def find_books_by_author(self, author):
        return [book for book in self.books if book.author == author]
    
    '''СОВЕРШЕННО НОВЫЙ ФУНКЦИОНАЛ'''
    def has_book(self, title):
        return any(book.title == title for book in self.books)

# Пример использования
library = Library() # Воплощаем в жизнь библиотеку
book1 = Book("1984", "George Orwell") # Вот какая есть книга
book2 = Book("To Kill a Mockingbird", "Harper Lee") # И такая

library.add_book(book1) # Взываешь к библиотеке что бы она вместила в себя книгу
library.add_book(book2) # И ещё одну

print("Список книг в библиотеке:") # !!! СОВЕРШЕННО НОВЫЙ ФУНКЦИОНАЛ !!!
library.list_books() # И умоляешь показать список

library.remove_book("1984") # !!! СОВЕРШЕННО НОВЫЙ ФУНКЦИОНАЛ !!!
print("\nПосле удаления '1984':") # !!! СОВЕРШЕННО НОВЫЙ ФУНКЦИОНАЛ !!!
library.list_books()

print("\nКниги автора 'Harper Lee':") # !!! СОВЕРШЕННО НОВЫЙ ФУНКЦИОНАЛ !!!
for book in library.find_books_by_author("Harper Lee"): # !!! СОВЕРШЕННО НОВЫЙ ФУНКЦИОНАЛ !!!
    print(book) # !!! СОВЕРШЕННО НОВЫЙ ФУНКЦИОНАЛ !!!

print("\nЕсть ли книга '1984' в библиотеке?", # !!! СОВЕРШЕННО НОВЫЙ ФУНКЦИОНАЛ !!!
      library.has_book("1984")) # !!! СОВЕРШЕННО НОВЫЙ ФУНКЦИОНАЛ !!!
