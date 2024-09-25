from dataclasses import make_dataclass

Account = make_dataclass('Account', ['id', 'name', 'balance'])

if __name__ == '__main__':
    # 測試物件創建
    michael = Account('0001', 'michael', 100)
    # 顯示物件
    print(michael)
    print(michael == Account('0001', 'michael', 100))
