import sys, os

def test_raise():
    try:
        result = 1 / 0 
    except Exception as e:
        file_name = os.path.basename(__file__) # 錯誤檔名
        line_no = sys.exc_info()[-1].tb_lineno # 錯誤發生行號
        raise Exception(f'{file_name} 第 {line_no} 行錯誤：不可以除以0 !!')

if __name__ == '__main__':
    # 測試
    try:
        test_raise()
    except Exception as e:
        print(f'錯誤：(10001) {e}')