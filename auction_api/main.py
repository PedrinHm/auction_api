# Análise de um exemplo de arquivo main.py para identificar problemas potenciais.

# Importando as bibliotecas e módulos necessários
from fastapi import FastAPI
from .routers import items, bids, users

# Criando uma instância do FastAPI
app = FastAPI()

# Incluindo os roteadores
app.include_router(items.router)
app.include_router(bids.router)
app.include_router(users.router)

# Definição da rota raiz
@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

# Verificação de inicialização direta para execução local
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
