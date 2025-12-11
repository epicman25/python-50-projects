from client import Client


class Bank:
    def __init__(self):
        self.bank_clients = {}

    def add_client(self, name):
        if name in self.bank_clients:
            print("Account already exists")
        else:
            self.bank_clients[name] = Client(name=name)

    def remove_client(self,name):
        if name in self.bank_clients:
            del self.bank_clients[name]

    def get_client(self, name):
        return self.bank_clients.get(name,None)
    
    def deposit(self,name,amount):
        if name not in self.bank_clients:
            return "Account does not exist"
        else:
            self.bank_clients[name].deposit(amount)

    def withdraw(self,name,amount):
        if name not in self.bank_clients:
            return "Account does not exist"
        else:
            self.bank_clients[name].withdraw(amount)

    def get_balance(self,name):
        if name not in self.bank_clients:
            return "Account does not exist"
        else:
            return self.bank_clients[name].check_balance()
