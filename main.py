from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Mundão!"}

@app.get("/detalhes")
def read_details():
    return {
        "nome" : "Pedro",
        "sobrenome" : "Silva",
        "idade" : 30,
    }
