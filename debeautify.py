import ASTParser
from linereader import linereader
import pymysql
import click

@click.command()
@click.argument('filename', nargs=1)

"""Program that algorithmically destroys your c code in unmaintainableness"""

def debeautify(filename):

    with open('filename', 'r') as content_file:
        filecontents = content_file.read()
    
    connector = pymysql.connect(host='34.207.179.27', port=3306, user='michael', passwd='mikerubbertoe', db='c_debeautify')
    curs = connector.cursor()
    
    ASTParser.parseFile(filecontents, curs) #prints to file temp.txt
    linereader(filename)

if __name__ == '__main__':
    debeautify()
