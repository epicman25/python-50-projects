class Client:

    def __init__(self,name):
        self.name = name
        self.balance = 0.0

    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.balance+=deposit_amount
            print(f"{deposit_amount} has been added to balance")
        else:
            raise ValueError("Deposit amount should be greater than zero")
        
    def withdraw(self, withdraw_amount):
        if withdraw_amount > 0:
            self.balance-=withdraw_amount
            print(f"{withdraw_amount} has been withdrawn from balance")     
        else:
            raise ValueError("Deposit amount should be greater than zero")
        
    def check_balance(self):
        return f"The balance of the account is : {self.balance}"



