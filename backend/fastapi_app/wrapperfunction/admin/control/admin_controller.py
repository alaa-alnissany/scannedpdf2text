
from fastapi import APIRouter
from wrapperfunction.admin.model import admin_models
import wrapperfunction.admin.service.admin_service as adminservice 

router = APIRouter


@router.get("/name")
def f1():

