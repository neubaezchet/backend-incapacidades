from fastapi import FastAPI
from app.routers import validate

app = FastAPI()

app.include_router(validate.router)

@app.get("/")
def root():
    return {"message": "API para validación de incapacidades médicas"}
