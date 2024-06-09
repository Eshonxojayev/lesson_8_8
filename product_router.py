from fastapi import APIRouter


product_router = APIRouter(prefix="/products")

@product_router.get("/")
async def get_orders():
    return {"message": "product page"}