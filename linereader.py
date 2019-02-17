import sys
import pymysql
import settings
from random import random, randint
from collections import namedtuple
from re import compile, search, match


def linereader(filename, varmap):

    #regex for finding functions
    func_pattern = compile("[A-Za-z0-9\*]+ [A-Za-z0-9]+\([A-Za-z0-9,*\[\] ]+\)")
     
    #open file into a list
    with open('temp.txt') as file:
        lines = file.read().splitlines()
    lines_annotated = []
    #namedtuple with line info, its scope in file, the type of line it contains and whether to add random code to it
    LineAnnotated = namedtuple('LineAnnotated', 
                               'line_string scope line_type random_add')
    #initialize loop variables
    current_scope = 0
    in_switch_struct = False 
    switch_struct_escape = -1
    current_line_type = ''    
    #iterate through list and generate unique annotations for properties of each line
    for counter, line in enumerate(lines):
        if not in_switch_struct:
            #check if keyword is in line and handle accordingly
            if func_pattern.search(line) and current_scope == 0:
                current_line_type = 'function'
            elif line.find('if') is not -1 or line.find('else') is not -1:
                current_line_type = 'ifelse'
            elif line.find('assert(') is not -1:
                current_line_type = 'assert'
            elif line.find('for') is not -1 or line.find('while') is not -1:
                current_line_type = 'loop'
            elif line.find('switch') is not -1 or line.find('struct') is not -1:
                in_switch_struct is True
                current_line_type = "switch" if line.find('switch') > 0 else "struct"
                switch_struct_escape = current_scope
                in_switch_struct = True
            else:
                current_line_type = ''
        #currently stuck in a switch
        else:
            current_line_type = 'switchorstruct'

        if line.find('}') is not -1:
            current_scope -= 1
            if switch_struct_escape == current_scope:
                in_switch_struct = False
        lines_annotated.append(LineAnnotated(line.strip(), current_scope,
                                             current_line_type, False))
        if line.find('{') is not -1:
            current_scope += 1
            
    settings.curglobal.execute("SELECT * from comments WHERE type='TODO';")
    TODOlist = []
    for item in settings.curglobal.fetchall():
        TODOlist.append(item[2])

    newfile = open('shitty_' + filename, "w")
    for line in settings.includes:
        newfile.write(line + '\n')
    for line in settings.defines:
        parts = line.split(' ')
        if parts[1] in varmap:
            parts[1] = varmap[parts[1]]
        for thing in parts:
            newfile.write(thing + ' ')
        newfile.write('\n')
    newfile.write('\n')
    
    for x, line_annotated in enumerate(lines_annotated):
        randomvar = randint(0,100)
        randi = randint(0,len(TODOlist)-1) 
        if line_annotated.line_type == 'assert':
            newfile.write('//NOT NEEDED NOW: ')
        newfile.write(''.join([line_annotated.scope * '    ' , 
                               line_annotated.line_string, 
                               " //TODO: " + TODOlist[randi] if randomvar <= (settings.probglobal / 2) else '' ,
                               "\n" ]))
    newfile.close()
