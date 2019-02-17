import pymysql

def init():
    connector = pymysql.connect(host='34.207.179.27', port=3306, user='michael', passwd='mikerubbertoe', db='c_debeautify')
    global curglobal
    curglobal = connector.cursor()
