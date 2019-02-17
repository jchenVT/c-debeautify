import ASTParser
from linereader import linereader
import pymysql
import click
import settings

@click.command()
@click.argument('filename', nargs=1)

def debeautify(filename):
    """Program that algorithmically destroys your c code in unmaintainableness"""

    settings.init()

    with open(filename, 'r') as content_file:
        filecontents = content_file.read()
    
    ASTParser.parseFile(filecontents, curs) #prints to file temp.txt
    linereader(filename)

if __name__ == '__main__':
    debeautify()
