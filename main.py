from fastapi import FastAPI

app = FastAPI(
    title="Demo API FastAPI",
    description="API de ejemplo para la asignatura",
    version="1.0"
)

usuarios = [
    {"id": 1, "nombre": "Emilio", "rol": "Admin"},
    {"id": 2, "nombre": "Ana", "rol": "Usuario"}
]

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando correctamente"}

@app.get("/usuarios")
def listar_usuarios():
    return usuarios

@app.get("/usuarios/{user_id}")
def obtener_usuario(user_id: int):
    for u in usuarios:
        if u["id"] == user_id:
            return u
    return {"error": "Usuario no encontrado"}