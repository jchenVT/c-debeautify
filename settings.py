import pymysql
import dev_settings as dev

def init():
    connector = pymysql.connect(host=dev.HOST, port=dev.PORT,
                                user=dev.USER, passwd=dev.PASSWORD, 
                                db='c_debeautify')
    global curglobal
    global defines
    global includes
    global probglobal
    global optglobal

    curglobal = connector.cursor()
    probglobal = 65
    defines = []
    includes = []
    optglobal = 0
