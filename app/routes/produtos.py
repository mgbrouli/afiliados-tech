from fastapi import APIRouter
from app.services.afiliados import buscar_produtos_mock

router = APIRouter(prefix="/api/produtos", tags=["Produtos"])

@router.get("/")
def listar_produtos():
    return buscar_produtos_mock()