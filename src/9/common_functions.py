def divide(a, b):
    try:
        result = a / b
        return result
    except Exception as e:
        print(f'錯誤：(10001) {e}')
        raise Exception(f'{file_name} 第 {line_no} 行錯誤：不可以除以0 !!')        
        return 0