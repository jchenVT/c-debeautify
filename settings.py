import pymysql
import dev_settings.py as dev

def init():
    connector = pymysql.connect(host=dev.HOST, port=dev.PORT,
                                user=dev.USER, passwd=dev.PASSWORD, 
                                db='c_debeautify')
    global curglobal
    curglobal = connector.cursor()
