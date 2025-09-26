
from fastapi import APIRouter, HTTPException
from admin.model import admin_models
import admin.service.admin_service as adminservice 

router = APIRouter()


@router.post("/name")
def f1(query:admin_models.UserQuery):
    try:
        return adminservice.reply(query)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
