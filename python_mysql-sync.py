#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
os.environ['PYTHON_EGG_CACHE'] = '/tmp/.python-eggs'
import sys,datetime,MySQLdb,socket,paramiko
def final_check_mysql():
    status = "true"
    try:
        conn = MySQLdb.Connect(host='xxx',port=3306,user='root',passwd='xxx',db='zabbix')
        cur = conn.cursor()
        cur.execute("show slave status;")
        result = cur.fetchall()
        io_thread = result[0][10]
        sql_thread = result[0][11]
        seconds_behind_master = result[0][32]
        #print  io_thread,sql_thread
        cur.close()
        conn.close()
    except Exception,e:
        print  Exception,":",e
    try:
        if io_thread=="Yes" and sql_thread=="Yes" and seconds_behind_master<=1000:
            return 1
        else:
            status = "false"
            return 0

    except Exception,e:
        print Exception,":",e
if __name__=='__main__':
    result=final_check_mysql()
    print result
