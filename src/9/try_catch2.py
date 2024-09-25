import traceback

try:
    result = 1 / 0 #除以0，發生錯誤
except Exception as e:
    print(f'錯誤：(10001) {e}')
    print(f'{"-"*10} 詳細內容 {"-"*10}')
    traceback.print_exc()
    print(f'{"-"*30}')
    