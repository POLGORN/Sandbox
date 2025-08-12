# =======================================================
# Open/Closed Principle
"""
Принцип открытости или закрытости утверждает что классы
должны быть открыты для расширения
и закрыты для модицикации
Иными словами поведение класса можно изменять не изменяя его
исходный код
...
Классы должны быть открыты для расширения но закрыты для модификации
"""
class Report:
    def generate(self):
        pass

class PDFReport(Report):
    def genetare(self):
        # Логика генерации PDF отчёта
        pass

class HTMLReport(Report):
    def generate(self):
        # Логика генерации HTML отчёта
        pass 
# =======================================================
""" НЕ ПРАВИЛЬНО """
class Order:
    def process_payment(self, payment_type):
        if payment_type == "налик":
            # Код который обрабатывает оплату наличными
    
        elif payment_type == "кредитка":
            # Код который обрабатывает оплату кредитной картой

        elif payment_type == "мобильник":
            # Код который обрабатывает оплату мобильным платежем
# =======================================================
""" ПРАВИЛЬНО """
class PaymentProcessor: # <--- Является интерфейсом
    def process_payment(self):
        # Метод который будет меняться в других методах

class CashPaymentProcessor(PaymentProcessor): # Наследуемый от PaymentProcessor
    # Меняем сходный метод
    def process_payment(self):
        # Код который обрабатывает оплату наличными

class CreditCardPaymentProcessor(PaymentProcessor): # Наследуемый от PaymentProcessor
    # Меняем сходный метод
    def process_payment(self):
        # Код который обрабатывает оплату кредитной картой

class MobilePaymentProcessor(PaymentProcessor): # Наследуемый от PaymentProcessor
    # Меняем сходный метод
    def process_payment(self):
        # Код который обрабатывает оплату мобильным платежем
# =======================================================
""" ТАК ТОЖЕ ПРАВИЛЬНО """
class Payment: # <--- Можно сказать что является абстрактным классом
    def process_payment(self):
        raise NotImplementedError("Subclasses should implement this method")

class CashPayment(Payment):
    def process_payment(self):
        # Код который обрабатывает оплату наличными
        print("Обработка оплаты наличными")

class CreditCardPayment(Payment):
    def process_payment(self):
        # Код который обрабатывает оплату кредитной картой
        print("Обработка оплаты кредитной картой")

class MobilePayment(Payment):
    def proocess_payment(self):
        # Код который обрабатывает оплату мобильным платежем
        print("Обработка оплаты мобильным платежем")

class Order:
    def process_payment(self, payment: Payment):
        payment.process_payment()
# =======================================================