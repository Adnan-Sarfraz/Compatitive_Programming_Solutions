class Bank:
    def __init__(self, balance, name):
        self.name=name
        self.__balance=balance

    def show_balance(self):
         print(f"{self.name}'s balance is {self.__balance}")

    def deposit(self, amount):
        self.__balance+=amount
        print(f"{amount} is added and new balance is {self.__balance}")


acc1=Bank(1000, "Adnan")
acc1.show_balance()
acc1.deposit(500)