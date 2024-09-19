import ast
import pprint
from graphviz import Digraph

# 使用 dot 語言描述圖形，使用GraphViz將dot轉為圖檔
def draw_ast(tree):
    def add_node(node, parent=None):
        node_name = str(node.__class__.__name__)
        dot.node(str(id(node)), node_name)
        if parent:
            dot.edge(str(id(parent)), str(id(node)))
        for child in ast.iter_child_nodes(node):
            add_node(child, node)
            
    dot = Digraph()
    add_node(tree)
    dot.format = 'png'
    dot.render('my_ast', view=True)

# AST 解析
code = 'a + b - 5'
tree = ast.parse(code)
pprint.pprint(ast.dump(tree))

# 繪製 AST
draw_ast(tree)




