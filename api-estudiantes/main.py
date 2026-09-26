from fastapi import FastAPI
from pydantic import BaseModel

# Creamos una instancia de FastAPI.
# La variable app representa nuestra aplicación.
app = FastAPI()


# GET indica el método HTTP.
# "/" indica la ruta.
@app.get("/")
def inicio():
    return {"mensaje": "Hola, esta es mi primera API"}


@app.get("/curso")
def obtener_curso():
    return {
        "nombre": "Fundamentos de Python",
        "modalidad": "En línea"
    }


# Recibe dos números y devuelve la suma.
@app.get("/sumar")
def sumar(numero1: float, numero2: float):
    resultado = numero1 + numero2

    return {
        "numero1": numero1,
        "numero2": numero2,
        "resultado": resultado
    }


# Clase que representa los datos que recibiremos en el Body.
class Numeros(BaseModel):
    numero1: float
    numero2: float


# Recibe dos números mediante JSON y devuelve la resta.
@app.post("/restar")
def restar(numeros: Numeros):
    resultado = numeros.numero1 - numeros.numero2

    return {
        "numero1": numeros.numero1,
        "numero2": numeros.numero2,
        "resultado": resultado
    }
    