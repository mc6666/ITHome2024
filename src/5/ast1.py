import ast
import pprint

code = 'a + b'
tree = ast.parse(code)
pprint.pprint(ast.dump(tree))

