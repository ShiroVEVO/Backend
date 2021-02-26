import peewee

from fastapi import APIRouter, HTTPException, Response, Request
from fastapi.responses import HTMLResponse
from Models.contactos import create_contact, delete_contact,get_contact #, list_contacts
from typing import Any, List
from pydantic import BaseModel
from pydantic.utils import GetterDict

#crea un prefijo para editar la ruta y todo objeto que use esto pondra por defecto el /contact

router_contacts = APIRouter(
    prefix="/contacts",
    tags=["contacts"]
)

#templates = Jinja2Templates(directory="templates")

class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res

class ContactModel(BaseModel):
    Id:int
    Nombre:str
    Apellido:str
    Email:str
    Telefono:str

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict

@router_contacts.post("/", response_model=ContactModel, summary= "create a new contact")
async def create(Nombre: str, Apellido: str, Email: str, Telefono:str):
    return await create_contact(Nombre = Nombre, Apellido = Apellido, Email = Email, Telefono = Telefono)

@router_contacts.delete("/remove/{Id}", summary="Delete an individual contact" , response_class=Response,
    responses={
        200: {"description": "Contact successfully deleted"},
        404: {"description": "Contact not found"},
    },
)
async def delete(Id: int):
    del_contact = delete_contact(Id)
    if del_contact is None:
        return Response(status_code=404)
    return Response(status_code=200)

@router_contacts.get("/view/{Id}", summary="View an individual contact", response_model=ContactModel)
async def view(Id: int):
    contact = get_contact(Id = Id)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact