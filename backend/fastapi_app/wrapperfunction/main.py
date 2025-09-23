from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Customer(BaseModel):
    name: Optional[str]
    age: Optional[int]
    phone: Optional[str]


@app.get("/")
def read_root():
    return {"message": "manyouk al dagageh "}

@app.get("/items/")
def read_item(item_id: int= 0, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/customer/{customer_id}")
def read_customer(customer_id: int, customer: Customer):
    return {
        "customer_id": customer_id,
        "customer": customer.name,
        }