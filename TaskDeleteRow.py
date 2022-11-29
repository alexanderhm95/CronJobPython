# coding=utf-8
# Llenar una tabla en una base de datos con 100 datos luego a las 02h00 se vaya eliminando el ultimo registro de la tablaLlenar una tabla en una base de datos con 100 datos luego a las 02h00 se vaya eliminando el ultimo registro de la tabla

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
	#obtenemos el ultimo id de la tabla
	cursor.execute("SELECT MAX(id) FROM persona")
	#obtenemos el ultimo id de la tabla
	ultimo_id = cursor.fetchone()
	#obtenemos el ultimo id de la tabla
	ultimo_id = ultimo_id[0]

	#Vamos a eliminar el ultimo registro de la tpythonabla
	cursor.execute("DELETE FROM persona WHERE id = %s", (ultimo_id,))
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
