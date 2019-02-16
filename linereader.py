import sys
import time
from random import random
from collections import namedtuple

def linereader(filename):
     
    with open(filename) as file:
        lines = file.read().splitlines()
    lines_annotated = []
    #namedtuple with line info, its scope in file, the type of line it contains and whether to add random code to it
    LineAnnotated = namedtuple('LineAnnotated', 'line_string scope line_type random_add')
    current_scope = 0
    in_switch_struct is false 
    current_line_type = ''    
    for counter, line in enumerate(lines):
        if not in_switch_struct:
            if line.find('if') is not -1 or line.find('else') is not -1:
                current_line_type = 'ifelse'
            elif line.find('#define') is not -1 or line.find('#include') is not -1:
                current_line_type = 'pound'
            elif line.find('for') is not -1 or line.find('while') is not -1:
                current_line_type = 'loop'
            elif line.find('switch') is not -1:
                in_switch_struct is True
                current_line_type = 'switch'
                switch_struct_escape = current_scope-1
            elif line.find('struct') is not -1:
                in_switch_struct is True
                current_line_type = 'struct'
                switch_struct_escape = current_scope-1
            else
                current_line_type = ''
        #make regex to search for array shit        
        lines_annotated[counter] = LineAnnotated(line, current_scope, current_line_type)
        if line.find('{') is not -1:
            current_scope += 1
        if line.find('}') is not -1:
            current_scope -= 1
            if switch_struct_escape == current_scope:
                in_switch_struct = False
            
    
    random_add_lines = []
    for x in range(0,lines_annotated.count):
        if random() < .15:
            

