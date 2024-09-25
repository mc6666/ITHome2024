from dataclasses import dataclass

@dataclass
class Account:
    id:str      # 帳號
    name:str    # 姓名
    balance:int = 0 # 帳戶餘額
    
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
    
    # 顯示物件
    print(michael)
    print(michael == Account('0001', 'michael', 100))
    print(michael == Account('0001', 'michael', 7100))
    
    michael_2 = Account('0001', 'michael', 'x')
    print(michael_2.balance)
    
    