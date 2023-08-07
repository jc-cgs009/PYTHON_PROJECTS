import mysql.connector


def connect_database(database_name=None):
    con_obj = mysql.connector.connect(host="localhost", user="root", passwd="Master#123", database=database_name)
    return con_obj

