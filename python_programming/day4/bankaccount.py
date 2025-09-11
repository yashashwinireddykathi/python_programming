class bank:
    def __init__(self,balance):
        self.__balance = balance 
    def deposit(self,amount):
        self.amount=amount
        self.__balance=self.__balance+self.amount
    def withdraw(self,amount):
        self.amount=amount
        if self.amount<=self.__balance:
            self.__balance=self.__balance-self.amount
        else:
            print("insufficient balance to withdraw")
    def get_balance(self):
        print("the current balance:",self.__balance)
class sb(bank):
    def __init__(self, balance):
        super().__init__(balance)
    def display(self):
        print(self.__balance)
b=bank(0)
b.deposit(10000)
b.withdraw(15000)
b.get_balance()
s=sb(1000)
s.display()
