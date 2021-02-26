from peewee import *

from Models.Base import BaseModel

class Contact(BaseModel):
    #Se usan los tipos de datos de peewee porque es el que va a hacer el mapeo
    Id = PrimaryKeyField(null = False)
    Nombre = CharField(max_length=45)
    Apellido = CharField(max_length=45)
    Email = CharField(max_length=45)
    Telefono = CharField(max_length=25)

    class Meta: #Hereda la base y especifica la tabla
        db_table = 'contactos'

#base de datos =  a lo que reciba del json
async def create_contact(Nombre:str, Apellido:str, Email:str, Telefono:str):
    contact_object = Contact(
        Nombre= Nombre,
        Apellido= Apellido,
        Email= Email,
        Telefono = Telefono
    )
    #funcion de peewee que guarda en la base de datos
    contact_object.save()
    return contact_object

async def delete_contact(Id:int):
    return contact_object.delete().where(Contact.Id == Id).execute()

async def get_contact(Id:int):
    return contact.filter(Contact.Id == Id).first()