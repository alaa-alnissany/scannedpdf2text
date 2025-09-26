from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from admin.control import admin_controller

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials= True, # Allow cookies/authorization headers
    allow_methods=["*"], # Allow all HTTP methods
    allow_headers=["*"], # Allow all headers
    )


app.include_router(
    admin_controller.router,
    prefix = "/api/v1/admin",
    tags = ["admin"],
    dependencies = None
    )

