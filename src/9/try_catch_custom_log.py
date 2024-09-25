from datetime import datetime
import os, logging

# 建立log資料夾
os.makedirs('log', exist_ok=True)  # Create the directory if it doesn't exist

# 自訂工作日誌(logger)
logger = logging.getLogger(__name__)

# 訂定 handlers
file_handler = logging.FileHandler(f"log/app.log", mode="a", encoding="utf-8")

# 指定logger的handlers
logger.addHandler(file_handler)

# 設定訊息欄位
formatter = logging.Formatter("{asctime} {levelname}:{message}\n-------- 詳細內容 ----------", 
    datefmt='%Y-%m-%d %I:%M:%S', style="{")
file_handler.setFormatter(formatter)

# 測試
try:
    result = 1 / 0 #除以0，發生錯誤
except Exception as e:
    print(f'錯誤：(10001) {e}')
    logger.exception(f'{e}')
