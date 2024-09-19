import ast
import operator

op_map = {
    # binary
    ast.Add: operator.__add__,
    ast.Sub: operator.__sub__,
    ast.Div: operator.__truediv__,
    ast.Mult: operator.__mul__,
    # unary
    ast.UAdd: operator.__pos__,
    ast.USub: operator.__neg__,
}

allowed_types = {int, float}

class evaluator():
    def __init__(self, **arg):
        self.arg = arg
    
    def calc(self, expr: str):
        return self.compute(ast.parse(expr, mode="eval").body)

    def compute(self, expr):
        match expr:
            case ast.Constant(value=value):
                if type(value) not in allowed_types:
                    raise SyntaxError(
                        f"Not a number {value!r}"
                    )
                return value
            case ast.UnaryOp(op=op, operand=value):
                try:
                    return op_map[type(op)](self.compute(value))  # type: ignore
                except KeyError:
                    raise SyntaxError(f"Unknown operation {ast.unparse(expr)}")
            case ast.BinOp(op=op, left=left, right=right):
                try:
                    return op_map[type(op)](self.compute(left), self.compute(right))  # type: ignore
                except KeyError:
                    raise SyntaxError(f"Unknown operation {ast.unparse(expr)}")
            case x:
                try:
                    value = self.arg[x.id] # 以字典取變數值
                    return value
                except KeyError:
                    raise SyntaxError(f"Invalid Node {ast.dump(x)}")