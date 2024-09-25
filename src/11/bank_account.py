class Account:
    def __init__(self, id, name, balance=0):
        self.id = id # 帳號
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
        
if __name__ == '__main__':
    # 測試物件創建
    michael = Account('0001', 'michael', 100)
    john = Account('0002', 'john', 0)
    mary = Account('0003', 'mary')
        
    # 呼叫類別的方法
    michael.deposit(10_000)
    michael.withdraw(3_000)
    print(michael.balance)
    
    