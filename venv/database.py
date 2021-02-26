from peewee import MySQLDatabase

user = 'root'
password = 'Onepiece345'
db_name = 'prueba'

conexion = MySQLDatabase(
   db_name,
   user=user,
   password=password,
   host='localhost'
)


