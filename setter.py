class bankaccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value
account1 = bankaccount("Alice", 1000)
print(f"Account holder: {account1.name}, Balance: {account1.balance}")
account1.balance = 500
print(f"Account holder: {account1.name}, Balance: {account1.balance}")
