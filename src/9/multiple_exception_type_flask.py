import sys
from flask import Flask, request
 
app = Flask(__name__)
 
@app.route("/", methods=['GET'])
def test1():
    # 開啟檔案
    try:
        f = open('./data.txt', encoding='utf8')
        content = f.read()
    except Exception as e:
        return f'錯誤：(10001) {e}'    

    # 計算
    try:
        a, b = int(content.split()[0]), int(content.split()[1]) 
        result = a / b
        return result
    except Exception as e:
        return f'錯誤：(10002) {e}'    
 
if __name__ == '__main__':
    app.run()

