from common_functions import divide

if __name__ == '__main__':
    # 測試
    try:
        c = divide(1, 0)
        print(c+5)
    except Exception as e:
        print(f'錯誤：(10001) {e}')