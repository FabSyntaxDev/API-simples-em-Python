from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Criamos uma variável global para armazenar o estado
db_temporario = {"item_nome": "Nenhum produto enviado"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite qualquer site acessar a API
    allow_credentials=True,
    allow_methods=["GET"], # pode Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"], 
)


# O que você espera receber
class Item(BaseModel):
    nome: str
    preco: float

@app.get("/")
def read_root():
    return {"message": "Hello Mundão!"}

@app.get("/detalhes")
def read_details():
    return {
        "nome" : "Pedro",
        "sobrenome" : "Silva",
        "idade" : 30,
        "Produto" : db_temporario["item_nome"],
    }

@app.post("/enviar")
def criar_item(item: Item):
    db_temporario["item_nome"] = item.nome
    return {"status": "recebido", "valor_total": item.preco}

