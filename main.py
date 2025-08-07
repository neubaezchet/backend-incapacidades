from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import validate

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(validate.router, prefix="/validate")

@app.get("/")
def read_root():
    return {"message": "Backend de validación de incapacidades activo."}
