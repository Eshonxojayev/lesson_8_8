from fastapi import FastAPI, security, HTTPException
from database import session, ENGINE
from order_router import order_router
from product_router import product_router

app = FastAPI()
app.include_router(order_router)
app.include_router(product_router)

@app.get("/")
async def landing():
    return {
        "message": "This is landing page"
    }