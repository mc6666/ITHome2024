from dataclasses import dataclass

@dataclass
class Account:
    id:str      # 帳號
    name:str    # 姓名
    balance:int # 帳戶餘額
    
    # 存款   
    def deposit(self, amount):
        # 測試 self
        # print(type(self))
        self.balance += amount
        
    # 提款   
    def withdraw(self, amount):
        self.balance -= amount

# 薪轉帳戶
@dataclass
class Wage_account(Account): # 繼承 Account
    company_id:str  # 公司代碼
    employee_id:str # 員工代碼
        
if __name__ == '__main__':
    # 測試物件創建
    michael = Wage_account('0001', 'michael', 100, 'TSMC', '2020010001')
    michael_2 = Wage_account(id='0001', name='michael', balance=100, 
        company_id='TSMC', employee_id='2020010001')
    
    # 顯示物件
    print(michael)
    print(michael_2)
    
    