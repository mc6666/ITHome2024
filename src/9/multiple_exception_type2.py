import sys

# 開啟檔案
try:
    f = open('./data.txt', encoding='utf8')
    content = f.read()
except Exception as e:
    print(f'錯誤：(10001) {e}')
    sys.exit(1)     

# 計算
try:
    a, b = int(content.split()[0]), int(content.split()[1]) 
    result = a / b
except Exception as e:
    print(f'錯誤：(10002) {e}')
    sys.exit(2)     

sys.exit(0)     
