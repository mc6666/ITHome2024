from datetime import datetime
import os, logging

# 建立log資料夾
os.makedirs('log', exist_ok=True)  # Create the directory if it doesn't exist

logger = logging.getLogger(__name__)
# 取得【年月日時分】的字串，作為檔名的一部分。
date_time = datetime.now().strftime("%Y_%m_%d_%H_%M")
# 設定工作日誌檔的檔名、欄位及內碼，及要寫入的等級
logging.basicConfig(filename=f'log/{date_time}.log', 
    format='%(asctime)s %(levelname)s:%(message)s', datefmt='%I:%M:%S', 
    encoding='utf-8', level=logging.DEBUG)

# 宣告Decorator函數
def log_decorator(func):
    # inner function
    def wrapper(): 
        logging.debug(f"呼叫函數{func.__name__}前")
        func()
        logging.debug(f"呼叫函數{func.__name__}後")
    # 呼叫 inner function
    return wrapper

# 為 say_hello 函數加上 Decorator
@log_decorator
def say_hello():
    print("hello !")
    
# 測試
say_hello()    