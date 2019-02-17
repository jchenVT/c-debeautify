from pycparser import c_generator, c_parser, c_ast

# internal use
src = r'''
int main()
{
    int i = 0;
    int arr[10];
    arr[i] = 1;
}
'''

class ArrayRefVisitor(c_ast.NodeVisitor):
    def visit_ArrayRef(self, node):
        x = node.name
        if isinstance(node.subscript, c_ast.ID):
            node.name = node.subscript
            node.subscript = x
        else:
            node.name = node.subscript
            node.subscript = x
        return node