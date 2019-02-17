import ASTParser
from linereader import linereader
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

if __name__ == '__main__':
    debeautify()
