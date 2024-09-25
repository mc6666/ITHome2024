from datetime import datetime
import os, logging

# 建立log資料夾
os.makedirs('log', exist_ok=True)  # Create the directory if it doesn't exist

logger = logging.getLogger(__name__)
# 取得【年月日時分】的字串，作為檔名的一部分。
date_time = datetime.now().strftime("%Y_%m_%d_%H_%M")
# 設定工作日誌檔的檔名、欄位及內碼，及要寫入的等級
logging.basicConfig(filename=f'log/{date_time}.log', 
    format='%(asctime)s %(levelname)s:%(message)s', datefmt='%Y-%m-%d %I:%M:%S', 
    encoding='utf-8', level=logging.DEBUG)

# 測試
try:
    result = 1 / 0 #除以0，發生錯誤
except Exception as e:
    print(f'錯誤：(10001) {e}')
    logging.exception(f'錯誤：(10001) {e}\n{"-"*10} 詳細內容 {"-"*10}')
