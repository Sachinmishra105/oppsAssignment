# Challenge 4: Implement a Banking Account.


class Account:
    def __init__(self,title=None,balance=0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self,title,balance,interestRate):
        self.title = title
        self.balance = balance
        self.interestrate = interestRate

    def Details(self):
        return (f'title is {self.title} and Balance is {self.balance} and Interest rate is {self.interestrate}')    


x =SavingsAccount("Ashish",500,5)
print(x.Details())

    
