import tkinter as tk # Импортируем библиотеку для GUI
from tkinter import messagebox # Импортируем метод для всплывающего окна

class View:
    def __init__(self, root):
        # Метод инициализации
        self.root = root
        self.root.title("Программа пустышка")
        self.root.geometry("400x300")

        # Приветственная метка
        self.label = tk.Label(root, text="Добро пожаловать", font=("Arial", 14))
        self.label.pack(pady=10)

        # Поле для ввода
        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        # Кнопка для действия
        self.button = tk.Button(root, text="Нажми меня")
        self.button.pack(pady=10)

        # Кнопка для выхода
        self.quit_button = tk.Button(root, text="Выход", command=root.quit)
        self.quit_button.pack(pady=10)

    def set_button_command(self, command):
        # Метод по установке того самого действия
        self.button.config(command=command)

    def show_message(self, message):
        # Метод для всплывающего окна
        messagebox.showinfo("Информация", message)

    def get_input(self):
        # Метод возврата того что ввёл пользователь
        return self.entry.get()