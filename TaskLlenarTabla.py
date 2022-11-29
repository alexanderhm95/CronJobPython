# coding=utf-8
# Respaldo de una base de datos a las 01h00 todos los dias

import mysql.connector
from mysql.connector import errorcode

try:
	cnx = mysql.connector.connect(user
		= 'alex',
		password
		= 'root1234',
		host
		= 'localhost',
		database
		= 'CronJobPython')
	cursor = cnx.cursor()
	#Vamos a elimina
	cursor.execute("SELECT MAX(id) FROM persona")
	#Obtenemos el ultimo id
	ultimo_id = cursor.fetchone()
	#Aumentamos el ultimo id en 1
	ultimo_id = ultimo_id[0]
	
	for i in range(1,100):
		datos = (str(ultimo_id+i),"Alex" + str(i),"root" + str(i))
		cursor.execute("INSERT INTO persona (id, name, pass) VALUES (%s, %s, %s)", datos)
		cnx.commit()
	cursor.close()
	cnx.close()
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something is wrong with your user name or password")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	else:
		print(err)
else:
	cnx.close()
