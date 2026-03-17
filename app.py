#import numpy
import pymssql

server = "willy0627.database.windows.net"
database = "free-sql-db-0798852"
user = "dbeng"
password = "Aa12345678"
#print("Import success")
connect = pymssql.connect(server,user,password,database)
print("Login success")

cursor = connect.cursor()
print("cursor取得成功")

cursor.execute("select * from stocks")