import json
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()



usuarios = []
contador_id = 1


class Usuario(BaseModel):
    nome: str
    idade: int


@app.get("/usuarios")
def listar_usuarios():
    return usuarios


@app.post("/usuarios")
def criar_usuario(usuario: Usuario):
    global contador_id

    novo_usuario = {
        "id": contador_id,
        "nome": usuario.nome,
        "idade": usuario.idade
    }

    usuarios.append(novo_usuario)
    contador_id += 1

    return novo_usuario


@app.put("/usuarios/{id}")
def atualizar_usuario(id: int, usuario: Usuario):
    for usuario_lista in usuarios:
        if usuario_lista["id"] == id:
            usuario_lista["nome"] = usuario.nome
            usuario_lista["idade"] = usuario.idade
            return {"mensagem": "Usuário atualizado", "usuario": usuario_lista}

    return {"erro": "Usuário não encontrado"}

@app.delete("/usuarios/{id}")
def deletar_usuario(id: int):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario)
            return {"mensagem": "Usuário deletado"}

    return {"erro": "Usuário não encontrado"}

@app.get("/")
def inicio():
    return {"mensagem": "API funcionando!"}