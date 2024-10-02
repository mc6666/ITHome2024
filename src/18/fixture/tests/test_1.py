import pytest
import sys, os

# 將路徑加入環境變數
sys.path.append(os.path.abspath(".."))

# 引用 main_program 資料夾的factorial函數
from src import Account

# Arrange
@pytest.fixture
def prepare_data():
    return [{'id':"0001", 'name':"john", 'balance':100, 'deposit':1000, 'withdraw':300, 'result':800},
            {'id':"0002", 'name':"mary", 'balance':500, 'deposit':200, 'withdraw':400, 'result':300}
            ]
            
# Account
def create_account(*prepare_data):
    account_list = []
    for item in prepare_data[0]:
        # print(item)
        account = Account(item['id'], item['name'], item['balance'])
        account.deposit(item['deposit'])
        account.withdraw(item['withdraw'])
        account_list.append(account)
    return account_list
    
def test_account_balance(prepare_data):
    # Act
    account_list = create_account(prepare_data)
    
    # Assert
    for item, result_item in zip(account_list, prepare_data):
        assert item.balance == result_item['result']