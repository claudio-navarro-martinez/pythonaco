import optparse
import random
import string
import sys
import threading
import time

try:
    import cx_Oracle
except:
    print("Failed to import cx_Oracle.so. LD_LIBRARY_PATH includes $ORACLE_HOME/lib.")
    sys.exit()

### Configuration Area ###

default_user = 'system'
default_password = 'austral1a'
default_ip = '192.168.1.73'
default_service = 'XE'

#####  Do not edit below unless you understand what you're doing  #####

if __name__ == "__main__":
    usage = './oraload.py [OPTIONS]'
    version = '0.9'

    ### Establish Connection as SYSDBA
    ### conn_sysdba = ''
    try:
        conn_sysdba = cx_Oracle.connect(default_user, default_password, default_ip + '/' + default_service, cx_Oracle.SYSDBA)
    except cx_Oracle.DatabaseError as cx_msg:
            print("[ERROR]\tFailed to connect to Database as sysdba.")
            print(cx_msg)
            sys.exit()

    ### Fetch candidate User List
    array_user_list = []
    if conn_sysdba:
        cur = conn_sysdba.cursor()
        sql = 'select username from dba_users'
        try:
            cur.execute(sql)
        except cx_Oracle.DatabaseError as cx_msg:
            print("[ERROR]\tFailed SQL: %s" % sql)
            print(cx_msg)
            sys.exit()
        rows = cur.fetchall()
        for row in rows:
            array_user_list.append(row[0])
        print(array_user_list)
        cur.close()

    if conn_sysdba:
        conn_sysdba.close()

