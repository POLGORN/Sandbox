# =======================================================
# Single Responsibility Principle
"""
Принцип едининственной ответственности гласит что через каждый класс
должна проходить одна и только одна ось изменений
иными словами у неё должна быть только одна функция
и только одна задача которую она выполняет 
...
Каждый класс должен иметь одну ответственность
"""
class Report:
    def generator(self):
        # Логика генерации отчёта
        pass

class ReportPrinter(self):
    def print(self, report):
        # Логика печати отчёта
        pass
# =======================================================
""" НЕ ПРАВИЛЬНО """
class Employee:
    # Конструктор класса
    def __init__(self, name, salary):
        self.employee_name = name # Имя сотрудника
        self.employee_salary = salary # Зарплата сотрудника

    def payroll(self):
        # Код который считает зарплату

    def generate_report(self):
        # Код который генерирует отчёт
# =======================================================
""" ПРАВИЛЬНО """
class Employee:
    def __init__(self, name, salary):
        self.employee_name = name # Имя сотрудника
        self.employee_salary = salary # Зарплата сотрудника

    def payroll(self):
        # Код который считает зарплату

class Reports:
    def generate_report(self, employee):
        # Код который генерирует отчёт 
# =======================================================   
""" ТАК ТОЖЕ ПРАВИЛЬНО """
class Employee:
    def __init__(self, name, salary):
        self.employee_name = name  # Имя сотрудника
        self.employee_salary = salary  # Зарплата сотрудника

class Payroll:
    def __init__(self, employee: Employee):
        self.employee = employee

    def calculate_salary(self):
        # Код, который считает зарплату
        return self.employee.employee_salary

class ReportGenerator:
    def __init__(self, employee: Employee):
        self.employee = employee

    def generate_report(self):
        # Код, который генерирует отчет
        return f"Employee Name: {self.employee.employee_name}, Salary: {self.employee.employee_salary}"
# =======================================================