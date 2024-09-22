import os, logging
from logging.handlers import SocketHandler, DEFAULT_TCP_LOGGING_PORT

# 自訂工作日誌(logger)
logger = logging.getLogger(__name__)

# 訂定 handlers
socketHandler = SocketHandler('localhost', DEFAULT_TCP_LOGGING_PORT)
# 指定logger的handlers
logger.addHandler(socketHandler)

# 設定等級
logger.setLevel("DEBUG")

# 測試
while True:
    msg = input('請輸入訊息:')
    if len(msg) == 0: break
    logger.debug(msg)
