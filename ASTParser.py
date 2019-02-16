from __future__ import print_function
import pymysql
import pycparser
from pycparser.c_ast import NodeVisitor
from pycparser import c_parser

variables = {}
functions = {}

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='c_debeautify')
cur = conn.cursor()



class DeclVisitor(NodeVisitor):
    def __init__(self):
        self.values = []

    def visit_Decl(self, node):
        #print(node)
        if not isinstance(node.type, pycparser.c_ast.FuncDecl):
            if node.name not in variables:
                cur.execute("SELECT * from variables ORDER BY RAND()LIMIT 1;")
                result = cur.fetchone()[1]

                while result in variables:
                    cur.execute("SELECT * from variables ORDER BY RAND()LIMIT 1;")
                    result = cur.fetchone()

                variables[node.name] = result
                #print(result)
            #print("isNotFunction")
            newName = variables[node.name]
            node.name = newName
            #node.type.declname = newName
        else:
            print("isFunction")


# text = r"""
#     typedef int Node, Hash;
#     void HashPrint(Hash* hash, void (*PrintFunc)(char*, char*))
#     {
#         unsigned int i;
#         if (hash == NULL || hash->heads == NULL)
#             return;
#         for (i = 0; i < hash->table_size; ++i)
#         {
#             Node* temp = hash->heads[i];
#             while (temp != NULL)
#             {
#                 PrintFunc(temp->entry->key, temp->entry->value);
#                 temp = temp->next;
#             }
#         }
#     }
# """

text = r'''
    void f(char * restrict joe){}
int main(void)
{
    unsigned int long k = 4;
    int p = k;
    int t[5];
    p = k;
    p = 2 + k + k + k;
    return 0;
}
'''

# Create the parser and ask to parse the text. parse() will throw
# a ParseError if there's an error in the code
#
parser = c_parser.CParser()
ast = parser.parse(text, filename='<none>')

cv = DeclVisitor()
cv.visit(ast)



# Uncomment the following line to see the AST in a nice, human
# readable way. show() is the most useful tool in exploring ASTs
# created by pycparser. See the c_ast.py file for the options you
# can pass it.

#ast.show(showcoord=True)
# OK, we've seen that the top node is FileAST. This is always the
# top node of the AST. Its children are "external declarations",
# and are stored in a list called ext[] (see _c_ast.cfg for the
# names and types of Nodes and their children).
# As you see from the printout, our AST has two Typedef children
# and one FuncDef child.
# Let's explore FuncDef more closely. As I've mentioned, the list
# ext[] holds the children of FileAST. Since the function
# definition is the third child, it's ext[2]. Uncomment the
# following line to show it:

#ast.ext[2].show()
ast.show()
# A FuncDef consists of a declaration, a list of parameter
# declarations (for K&R style function definitions), and a body.
# First, let's examine the declaration.

# function_decl = ast.ext[0].decl
# function_decl.show();

# for func_def in ast.ext:
#     #print("old name: %s\t new name: %s" % (func_def.decl.name, "test"))
#     #func_def.decl.name = "test"
#     func_def.decl.type.type.declname = "test"
#
#     for var_def in func_def.body:
#
#         #NEED TO CHECK UNARY AND BINARY OPERATIONS IN THE OPERATIONS OR IF IT IS JUST ASSIGNING IT TO A VARAIBLE
#         if isinstance(var_def, pycparser.c_ast.Decl):
#             #print(var_def.type.declname)
#             var_def.type.declname = "testing"
#
#         elif isinstance(var_def, pycparser.c_ast.Assignment):
#             #print("%s %s" % (var_def.lvalue.name, var_def.rvalue.name))
#             var_def.lvalue.name = "testing"
#
#
#             #NEED TO RECURSIVELY CHECK TO SEE IF THERE ARE MORE BINARY OPERATIONS
#             # if isinstance(var_def.rvalue, pycparser.c_ast.BinaryOp):
#             #     #print(var_def.rvalue.right)
#             #     if hasattr(var_def.rvalue.left, "name"):
#             #         print("is variable")
#             #     if hasattr(var_def.rvalue.right, "name"):
#             #         var_def.rvalue.right.name = "testing"
#             # elif hasattr(var_def.rvalue, "name"):
#             #     var_def.rvalue.name = "name"
#         #print(counter)
#
# #ast.show()

#generator = c_generator.CGenerator()
#print(generator.visit(ast))
#for test in function_decl:
#    print('name: %s\n' % test.name)

# function_decl, like any other declaration, is a Decl. Its type child
# is a FuncDecl, which has a return type and arguments stored in a
# ParamList node


#function_decl.type.args.show()

# The following displays the name and type of each argument:
#function_decl.type.show()
#for param_decl in function_decl.type.args.params:
#    print('Arg name: %s' % param_decl.name)
#   print('Type:')
#    param_decl.type.show(offset=6)
