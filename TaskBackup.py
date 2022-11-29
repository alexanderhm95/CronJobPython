# coding=utf-8
# Respaldo de una base de datos a las 01h00 todos los dias

import os
import time

DB_USER = 'alex'
DB_PASSWORD = 'root1234'
DB_NAME = 'CronJobPython'
BACK_DIR = '/home/alexanderhm/Escritorio/CronJobPython/'
TODAY = time.strftime('%Y-%m-%d -%H-%M-%S') # -%H-%M-%S
TODAY_DIR = BACK_DIR + TODAY

def backupsql():
	 # Si el directorio no existe, cree un nuevo directorio
	if not os.path.exists(TODAY_DIR):
		os.makedirs(TODAY_DIR)
	 # Ejecute el comando mysql para exportar la base de datos a un nuevo archivo
	sqlcmd = "mysqldump -u" + DB_USER + " -p" + DB_PASSWORD + " " + DB_NAME + " > " + TODAY_DIR + "/" + DB_NAME + ".sql"
	os.system(sqlcmd)

 # Función principal
def main():
	backupsql()

 # Ejecutar función principal
if __name__ == '__main__':
	main()

