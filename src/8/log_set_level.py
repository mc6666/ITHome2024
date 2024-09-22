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
    encoding='utf-8', level=logging.INFO)

# 測試
logging.info("set level to INFO")
logging.debug("除錯")
logging.info("資訊")
logging.warning("警告")
logging.error("錯誤")
logging.critical("關鍵資訊")

logging.getLogger().setLevel(logging.DEBUG) # 修改等級

# 測試
logging.debug("set level to DEBUG")
logging.debug("除錯")
logging.info("資訊")
logging.warning("警告")
logging.error("錯誤")
logging.critical("關鍵資訊")