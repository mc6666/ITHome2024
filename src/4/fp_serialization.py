from operator import add, sub, mul, truediv
import joblib

# 建立+-*/對應add, sub, mul, truediv函數的字典
operators = list('+-*/')
func_list = [add, sub, mul, truediv]
operators_dict = {operators[i]: func_list[i] for i in range(len(operators))}

# 序列化(Serialization)存檔
joblib.dump(operators_dict, 'operator.joblib')

# 反序列化(Deserialization)，自檔案載入
operators_dict2 = joblib.load('operator.joblib')

def perform_operation(op_string, a, b):
    return operators_dict2[op_string](a, b)

print(perform_operation('+', 100, 10))