# Challenge 5: Handling a Bank Account.

class Account:
    def __init__(self,title=None,balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self,amount):
        self.amount = amount
        self.balance = self.balance - self.amount
        return (f'Amount Withdrawal {self.amount} Remaining Balance {self.balance}')

    def Deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount 
        return (f'Deposit Amount {self.amount} Total Balance {self.balance}')

    def getBalance(self):
        return (f'remaining balance = {self.balance}')


class SavingsAccount(Account):
    def __init__(self,title=None,balance=0,interestRate=0):
        super().__init__(title,balance)
        self.interestRate = interestRate

    def interestamount(self):
        return (self.interestRate*self.balance)/100


obj = SavingsAccount("Ashish",5000,5)
print(obj.title)
print(obj.balance)
print(obj.withdrawal(500))
print(obj.Deposit(10000))
print(obj.getBalance())
print(obj.interestamount())              

    


