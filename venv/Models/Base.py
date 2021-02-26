from peewee import *

from database import conexion

#Permite mandarle la conexion a la base de datos,
class BaseModel(Model):
    class Meta:
        database = conexion

