

class Account:

    def __init__(self,filepath):
        self.filepath = filepath
        with open(filepath,'r') as balance_file:
            self.balance=int(balance_file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount
        
    def deposit(self,amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath,"w+") as balance_file:
            balance_file.write(str(self.balance))



account = Account("balance.txt")
print(account.balance)         
account.deposit(2200)
print(account.balance)         
account.commit()
print(account.balance)