from fastapi import APIRouter

router = APIRouter(
    prefix="/validate",
    tags=["Validación de Incapacidades"]
)

@router.get("/test")
def test_validation():
    return {"message": "Ruta de validación funcionando correctamente"}
