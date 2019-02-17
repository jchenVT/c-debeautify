import ASTParser
from linereader import linereader
import re
import pymysql
import click
import settings
from os import remove

@click.command()
@click.argument('filename', nargs=1)
@click.options('--prob', type=click.IntRange(0,100))

def debeautify(filename, prob):
    """Program that algorithmically destroys your c code in unmaintainableness"""

    settings.init()
    settings.probglobal = prob

    with open(filename, 'r') as content_file:
        filecontents = content_file.read()
    
    ASTParser.parseFile(filecontents) #prints to file temp.txt
    linereader(filename)

    remove('temp.txt')

def pre_debeautify(filename):
    with open(filename, 'r+') as content_file:
        text = content_file.read()

    for line in content_file:
        if line[0] == '#':
            settings.includes.append(line)

    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " " # note: a space and not an empty string
        else:
            return s
    regret = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    to_write = re.sub(regret, replacer, text)
    content_file.write(re.sub(regret, replacer, text))


# comment_remover("shitty_example.c")

if __name__ == '__main__':
    debeautify()
