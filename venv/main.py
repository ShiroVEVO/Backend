from fastapi import FastAPI
from database import *
from routers import Contacto

#a


app = FastAPI(title ='contactos.py', descripcion='aaaa', version='0.1')

#eventos de fastapi que establecen la conexion apenas se inicia el servidor y la cierran apenas se apaga

@app.on_event("startup")
async def startup():
    print("Conectando...")
    if conexion.is_closed():
        conexion.connect()

@app.on_event("shutdown")
async def shutdown():
    print("Cerrando...")
    if not conexion.is_closed():
        conexion.close()

@app.get("/")
async def root():
    return {"message":"Contact Applications!"}

app.include_router(Contacto.router_contacts)