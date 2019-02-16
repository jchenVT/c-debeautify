from __future__ import print_function
import pymysql
import pycparser
from pycparser.c_ast import NodeVisitor
from pycparser import c_parser, c_generator

variables = {}
functions = {'main' : 'main'}

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='c_debeautify')
cur = conn.cursor()

#checks to see if the variable being looked at has already been renamed or not
def checkVariableInitalized(node):
    # checks to see if variable has been renamed already. If not, pick an unused name at random, add it to the dict and
    # If so, just return the name that is currently assigned
    if node.name not in variables:
        cur.execute("SELECT * from variables ORDER BY RAND()LIMIT 1;")
        result = cur.fetchone()[1]

        while result in variables:
            cur.execute("SELECT * from variables ORDER BY RAND()LIMIT 1;")
            result = cur.fetchone()[1]

        variables[node.name] = result
        return result
    return variables[node.name]

#checks to see if the function being looked at has already been renamed, ignoring main as that will make programs not run.
def checkFunctionInitialized(node):
    x = node.name
    if x not in functions:
        cur.execute("SELECT * from functions ORDER BY RAND()LIMIT 1;")
        result = cur.fetchone()[1]

        while result in functions:
            cur.execute("SELECT * from functions ORDER BY RAND()LIMIT 1;")
            result = cur.fetchone()[1]

        functions[node.name] = result
        return result
    return functions[node.name]

#class that walks through the AST to find all the nodes that are of ID type. These are used in operations and assignment
#statments
class IDVisistor(NodeVisitor):
    def visit_ID(self, node):
        newName = checkVariableInitalized(node)
        node.name = newName

#class that walks through the AST to find all the nodes that are of Decl type. These are the function and variable
#declrations
class DeclVisitor(NodeVisitor):

    def visit_Decl(self, node):

        #checks to see if the node is a function declaration
        if isinstance(node.type, pycparser.c_ast.FuncDecl):

            #get a new name for the function and rename the appropriate locations
            newName = checkFunctionInitialized(node)
            node.name = newName
            node.type.type.declname = newName

            #find the parameters for the function and rename them as well
            for node in node.type.args.params:
                if node.name is not None:
                    newName = checkVariableInitalized(node)
                    node.name = newName
                    while not isinstance(node.type, pycparser.c_ast.TypeDecl):
                        node = node.type
                    node.type.declname = newName

        #checks to see if the node is an array declaration and change the name of the array
        elif isinstance(node.type, pycparser.c_ast.ArrayDecl):
            newName = checkVariableInitalized(node)
            node.name = newName
            node.type.type.declname = newName

        #otherwise its a regular variable and change the name of it appropriately
        else:
            newName = checkVariableInitalized(node)
            node.name = newName
            node.type.declname = newName

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
    void f(char * restrict joe, int tram){}
int main(void)
{
    unsigned int long test1 = 4;
    int test2 = test1;
    int test3[test1];
    test2 = test1;
    test2 = 2 + test1 + test1 + test1;
    return 0;
}
'''

parser = c_parser.CParser()
ast = parser.parse(text, filename='<none>')

#ast.show()

dv = DeclVisitor()
idv = IDVisistor()
dv.visit(ast)
idv.visit(ast)

#ast.show()

generator = c_generator.CGenerator()
print(generator.visit(ast))
