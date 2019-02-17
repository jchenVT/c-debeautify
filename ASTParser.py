from __future__ import print_function
import pymysql
import pycparser
from pycparser.c_ast import NodeVisitor
from pycparser import c_parser, c_generator

variables = {'NULL' : 'NULL'}
functions = {'main' : 'main'}
ignore = {}

#connect to sql server where names are stored
conn = pymysql.connect(host='34.207.179.27', port=3306, user='michael', passwd='mikerubbertoe', db='c_debeautify')
cur = conn.cursor()

#checks to see if the variable being looked at has already been renamed or not
def checkVariableInitalized(node):
    # checks to see if variable has been renamed already. If not, pick an unused name at random, add it to the dict and
    # If so, just return the name that is currently assigned
    if node.name in functions.values():
        return node.name

    if node.name in ignore:
        return node.name

    if node.name not in variables:
        cur.execute("SELECT * from variables ORDER BY RAND()LIMIT 1;")
        result = cur.fetchone()[1]

        while result in variables:
            cur.execute("SELECT * from variables ORDER BY RAND()LIMIT 1;")
            result = cur.fetchone()[1]

        variables[node.name] = result
        return result

    if node.name not in variables:
        return node.name
    return variables[node.name]

#checks to see if the function being looked at has already been renamed, ignoring main as that will make programs not run.
def checkFunctionInitialized(node):
    x = node.name
    if node.name not in ignore and x not in functions:
        cur.execute("SELECT * from functions ORDER BY RAND()LIMIT 1;")
        result = cur.fetchone()[1]

        while result in functions:
            cur.execute("SELECT * from functions ORDER BY RAND()LIMIT 1;")
            result = cur.fetchone()[1]

        functions[node.name] = result
        return result

    if node.name not in functions:
        return node.name
    return functions[node.name]

#class that walks through the AST to find all the nodes that are of ID type. These are used in operations and assignment
#statments
class IDVisistor(NodeVisitor):
    def visit_ID(self, node):
        newName = checkVariableInitalized(node)
        node.name = newName

#visits all the struct to make sure that the reference to the struct is not overwritten
class StructRefVisistor(NodeVisitor):
    def visit_StructRef(self,node):
        #print(node)
        variables[node.field.name] = node.field.name
        while isinstance(node.name, pycparser.c_ast.StructRef):
            node = node.name
            variables[node.field.name] = node.field.name

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
            if node.type.args is not None:
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
            while not isinstance(node.type, pycparser.c_ast.TypeDecl):
                node = node.type
            node.type.declname = newName

class FuncCallVisitor(NodeVisitor):
    def visit_FuncCall(self, node):
        if node.name.name not in functions:
            ignore[node.name.name] = node.name.name
        else:
            node.name.name = functions[node.name.name]



# text = r'''
#     void f(char * restrict joe, int tram){}
# int main(void)
# {
#     unsigned int long test1 = 4;
#     int test2 = test1;
#     int test3[test1];
#     test2 = test1;
#     test2 = 2 + test1 + test1 + test1;
#     return 0;
# }
# '''

text = r'''
double getAverage(int arr[], int size);


int main(void)
{
	int array[] = {1, 2, 3, 4, 5, 6};
	int size = 6;
	double average;
	average = getAverage(array, size);
	printf("The average of the array is %f\n", average);
	return 0;
}


double getAverage(int arr[], int size)
{
	double average = 0;	
	for(int i=0; i<size; i++)
	{
		average += arr[i];
	}
	average = average/size;
	
	return average;
}


 '''
def parseFile():
    parser = c_parser.CParser()
    ast = parser.parse(text, filename='<none>')

    #ast.show()

    dv = DeclVisitor()
    idv = IDVisistor()
    srv = StructRefVisistor()
    fcv = FuncCallVisitor();
    srv.visit(ast)
    dv.visit(ast)
    fcv.visit(ast)
    idv.visit(ast)

    #ast.show()

    generator = c_generator.CGenerator()
    print(generator.visit(ast))
