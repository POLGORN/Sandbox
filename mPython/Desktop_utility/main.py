import tkinter as tk
from controller import Controller

if __name__ == "__main__":
    root = tk.Tk()
    app = Controller(root)
    root.mainloop()
# ________________________________________
# import tkinter as tk  # Импортируем библиотеку tkinter для создания графического интерфейса
# from controller import Controller  # Импортируем класс Controller из модуля controller

# # Проверяем, является ли этот файл основным модулем
# if __name__ == "__main__":
#     root = tk.Tk()  # Создаем корневое окно приложения
#     app = Controller(root)  # Создаем экземпляр контроллера, передавая корневое окно
#     root.mainloop()  # Запускаем главный цикл обработки событий