from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def payment(self,amount):
        pass

class CraditCard(Payment):
    def payment(self, amount):
        print(f"paid {amount} using cradit card")

class PayPal(Payment):
    def payment(self, amount):
        print(f"paid {amount} using the paypal")
              
cradit=CraditCard()
pay=PayPal()
cradit.payment(500)
pay.payment(500)