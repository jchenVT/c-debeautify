import ASTParser
from linereader import linereader
import re
import pymysql
import click
import settings
from os import remove

@click.command()
@click.argument('filename', nargs=1)
@click.option('--prob', default=65, show_default=True, type=click.IntRange(0,100))

def debeautify(filename, prob):
    """Program that algorithmically destroys your c code in unmaintainableness"""

    settings.init()
    settings.probglobal = prob

    filecontents = pre_debeautify(filename)
    
    varmap = ASTParser.parseFile(filecontents) #prints to file temp.txt
    linereader(filename, varmap)

    remove('temp.txt')

def pre_debeautify(filename):
    with open(filename, 'r') as content_file:
        text = content_file.read()
    temptext = []
    for line in text.split('\n'):
        if "#include" in line:
            print(line)
            settings.includes.append(line)
        elif "#define" in line:
            settings.defines.append(line)
            print(line)
        else:
            temptext.append(line)
    text = '\n'.join(temptext)
    text = comment_remover(text)
    return text


def comment_remover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " " # note: a space and not an empty string
        else:
            return s
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)


if __name__ == '__main__':
    debeautify()
