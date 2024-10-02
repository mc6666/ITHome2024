import unittest
from unittest.mock import Mock
import requests
from requests.exceptions import Timeout
from dataclasses import dataclass

@dataclass
class Response:
    status_code:int
    json:str
    
# 以 Mock 取代原本的 requests
requests = Mock()
requests.get.return_value = Response(status_code=200, json={'data':'wondful'})

def get_holidays():
    r = requests.get("http://localhost/api/holidays")
    if r.status_code == 200:
        return r.json
    return None

class TestHolidays(unittest.TestCase):
    def test_get_holidays_timeout(self):
        # 測試網路連線
        print(get_holidays())

if __name__ == "__main__":
    unittest.main()