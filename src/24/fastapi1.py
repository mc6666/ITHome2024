from fastapi import FastAPI

# 建立 FastAPI 物件
app = FastAPI()

# 設定路由及其處理函數
@app.get("/")
async def root():
    return {"message": "Hello World"}