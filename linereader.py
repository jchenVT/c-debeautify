import sys
import time
from random import random, randint
from collections import namedtuple
from re import compile, search, match


def linereader(filename):
    #regex for finding functions
    func_pattern = compile("[A-Za-z0-9\*]+ [A-Za-z0-9]+\([A-Za-z0-9,*\[\] ]+\)")
     
    with open(filename) as file:
        lines = file.read().splitlines()
    lines_annotated = []
    #namedtuple with line info, its scope in file, the type of line it contains and whether to add random code to it
    LineAnnotated = namedtuple('LineAnnotated', 'line_string scope line_type random_add')
    current_scope = 0
    in_switch_struct = False 
    switch_struct_escape = -1
    current_line_type = ''    
    for counter, line in enumerate(lines):
        if not in_switch_struct:
            if func_pattern.search(line) and current_scope == 0:
                current_line_type = 'function'
            elif line.find('if') is not -1 or line.find('else') is not -1:
                current_line_type = 'ifelse'
            elif line.find('assert(') is not -1:
                current_line_type = 'assert'
            elif line.find('#define') is not -1 or line.find('#include') is not -1:
                current_line_type = 'pound'
            elif line.find('for') is not -1 or line.find('while') is not -1:
                current_line_type = 'loop'
            elif line.find('switch') is not -1 or line.find('struct') is not -1:
                in_switch_struct is True
                current_line_type = "switch" if line.find('switch') > 0 else "struct"
                switch_struct_escape = current_scope
                in_switch_struct = True
            else:
                current_line_type = ''
        else:
            current_line_type = 'switchorstruct'

        if line.find('}') is not -1:
            current_scope -= 1
            if switch_struct_escape == current_scope:
                in_switch_struct = False
        lines_annotated.append(LineAnnotated(line, current_scope, current_line_type, False))
        if line.find('{') is not -1:
            current_scope += 1
            
    
    random_add_lines = []
    newfile = open('annotated_' + filename, "w")
    for x, line_annotated in enumerate(lines_annotated):
        randomvar = random()
        print(randomvar)
        if randomvar < .25:
            if line_annotated.line_type == '':
                temp_line = line_annotated
                temp_line.random_add == True
                lines_annotated[x] = temp_line

        #newfile.write(line_annotated.scope * '    ' line_annotated.line_string , ' //type: ' , line_annotated.line_type , ', randomadd: ' , line_annotated.random_add]))
        newfile.write(''.join([line_annotated.scope * '    ' , line_annotated.line_string , ' //type: ' , line_annotated.line_type , ', randomadd: {}'.format(line_annotated.random_add), '\n']))
    newfile.close()

if __name__ == '__main__':
    linereader('student.c')
