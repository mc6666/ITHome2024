import unittest
from unittest.mock import Mock
import requests
from requests.exceptions import Timeout

# 以 Mock 取代原本的 requests
requests = Mock()

def get_holidays():
    r = requests.get("http://localhost/api/holidays")
    if r.status_code == 200:
        return r.json()
    return None

class TestHolidays(unittest.TestCase):
    def test_get_holidays_timeout(self):
        # 設定呼叫 requests.get 會發生 Timeout 例外
        requests.get.side_effect = Timeout 
        # 若發生 Timeout 例外，執行縮排程式碼
        with self.assertRaises(Timeout):
            print('call get_holidays')
            print(get_holidays())

if __name__ == "__main__":
    unittest.main()