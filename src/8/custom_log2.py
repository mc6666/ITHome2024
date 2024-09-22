import os, logging

# 建立log資料夾
os.makedirs('log', exist_ok=True)  

# 自訂工作日誌(logger)
logger = logging.getLogger(__name__)

# 訂定 handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(f"log/app2.log", mode="a", encoding="utf-8")

# 指定logger的handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 顯示handlers及工作日誌預設等級
print(f'handlers：{logger.handlers}')
print(f'default level：{logger.level}')
print(f'EffectiveLevel：{logger.getEffectiveLevel()}')

# 設定等級
logger.setLevel("DEBUG")
console_handler.setLevel("DEBUG")
file_handler.setLevel("WARNING")

# 設定訊息欄位
formatter = logging.Formatter("{levelname} - {message}", style="{")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 測試
logger.debug("除錯")
logger.info("資訊")
logger.warning("警告")
