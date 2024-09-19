from asteval import Interpreter

aeval = Interpreter()
code = """def func(a, b):
    return a + b - 5
"""
aeval(code)
print(aeval("func(10, 2)"))