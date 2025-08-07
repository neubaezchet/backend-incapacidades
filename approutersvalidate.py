from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/upload")
async def upload_incapacidad(
    tipo: str = Form(...),
    cedula: str = Form(...),
    email: str = Form(...),
    files: list[UploadFile] = File(...)
):
    return JSONResponse(content={
        "tipo": tipo,
        "cedula": cedula,
        "email": email,
        "archivos_recibidos": [file.filename for file in files]
    })
