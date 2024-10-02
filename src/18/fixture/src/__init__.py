class Account:
    def __init__(self, id, name, balance=0):
        self.pid = id # 帳號
        self.name = name # 姓名
        self.balance = balance # 帳戶餘額
    
    # 存款   
    def deposit(self, amount):
        # 測試 self
        # print(type(self))
        self.balance += amount
        
    # 提款   
    def withdraw(self, amount):
        self.balance -= amount