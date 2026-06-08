from fastapi import FastAPI
from database import Base,engine
from routers import users,documents,rag
app=FastAPI(title="Financial Document AI System")
Base.metadata.create_all(engine)
app.include_router(users.router)
app.include_router(documents.router)
app.include_router(rag.router)
@app.get("/")
def home(): return {"message":"Financial AI Document Management API"}
