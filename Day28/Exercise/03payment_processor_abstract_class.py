# Exercise 3: Abstract Payment Processor

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processed credit card payment of ${amount}."

    def refund(self, amount):
        return f"Refunded ${amount} to credit card."

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processed PayPal payment of ${amount}."

    def refund(self, amount):
        return f"Refunded ${amount} to PayPal account."
 
payment_processors = [CreditCardProcessor(), PayPalProcessor()]
for processor in payment_processors:
    print(processor.process_payment(100))
    print(processor.refund(50))
