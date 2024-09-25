x = -1

try:
    if x <= 0:
        raise Exception('訂購數量不得小於或等於0 !!')
except Exception as e:
    print(f'錯誤：(10001) {e}')