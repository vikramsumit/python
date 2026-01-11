# Create an abstract class "PaymentGateway" with abstract methods for payment-related operations like process_payment() and refund_payment(). Create concrete subclasses for different payment gateways (e.g., "PayPal," "Stripe") and implement these methods to interact with the respective payment systems.

from abc import ABC, abstractmethod

class PaymentGateway:
    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def refund_payment(self, amount):
        pass

class Paypal(PaymentGateway):
    def process_payment(self, amount):
        print(f"processing payment of ${amount} via Paypal.....")
        return True
    
    def refund_payment(self, amount):
        print(f"Processing refund of ${amount} via Paypal.....")
        return True
    
class Stripe(PaymentGateway):
    def process_payment(self, amount):
        print(f"processing payment of ${amount} via Stripe.....")
        return True
    
    def refund_payment(self, amount):
        print(f"Processing refund of ${amount} via Stripe.....")
        return True
    
paypal = Paypal()
paypal.process_payment(5000)
paypal.refund_payment(4500)

stripe = Stripe()
stripe.process_payment(80000)
stripe.refund_payment(80000)

