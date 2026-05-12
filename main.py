from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite qualquer site (incluindo seu localhost)
    allow_credentials=True,
    #allow_methods=["*"], # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"], 
)

@app.get("/")
def read_root():
    return {"message": "Hello Mundão!"}

@app.get("/detalhes")
def read_details():
    return {
        "nome" : "Pedro",
        "sobrenome" : "Silva",
        "idade" : 30
    }
