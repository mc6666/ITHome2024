import ast
import operator

operators_dict = {
    # binary
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Div: operator.truediv,
    ast.Mult: operator.mul,
    # unary
    ast.UAdd: operator.__pos__,
    ast.USub: operator.__neg__,
}

allowed_types = {int, float}

def compute(expr):
    match expr:
        case ast.Constant(value=value):
            return value
        case ast.UnaryOp(op=op, operand=value):
            try:
                if type(value) in allowed_types: return value
                return compute(value) if op == '+' else 0-compute(value)
            except KeyError:
                raise SyntaxError(f"Unknown operation {ast.unparse(expr)}")
        case ast.BinOp(op=op, left=left, right=right):
            try:
                # print(f'op={ast.dump(op)}, left={ast.dump(left)}, right={ast.dump(right)}')
                return operators_dict[type(op)](compute(left), compute(right))
            except KeyError:
                raise SyntaxError(f"Unknown operation {ast.unparse(expr)}")
        case x:
            # try:
            value = eval(x.id)
            return value
            # except KeyError:
                # raise SyntaxError(f"Invalid Node {ast.dump(x)}")

a = 10
b = 2
code = 'a + b - 5'
tree = ast.parse(code, mode="eval").body
print(compute(tree))