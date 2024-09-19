from evaluator_lib import evaluator

code = 'a + b - 5'
obj = evaluator(a=10, b=2)
print(obj.calc(code))