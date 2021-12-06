import mysql.connector
from mysql.connector import Error

try:
	connection = mysql.connect.connect(host = 'mariadb', database = 'ncatparking')
	
	if connection.is_connected():
	database_info = connection.get_server_info()
	print("Connected to MYSQL Server version", database_info)
	cursor = connection.cursor()
	cursor.execute("select database();")
	record = cursor.fetchone()
	print("Connected to the database: ", record)
	
except Error as e:
	print("Unable to connect to MYSQL", e)
	
finally:
	if connection.is_connected():
	cursor.close()
	connection.close()
	print("The MYSQL server is now closed")