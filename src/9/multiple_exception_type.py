try:
    f = open('./data.txt', encoding='utf8')
    content = f.read()
    a, b = int(content.split()[0]), int(content.split()[1]) 
    result = a / b
except FileNotFoundError as e:
    print(f'錯誤：(10001) {e}')
except ValueError as e:
    print(f'錯誤：(10002) {e}')
except ZeroDivisionError as e:
    print(f'錯誤：(10003) {e}')
except Exception as e:
    print(f'錯誤：(10004) {e}')