from pydantic import BaseModel
from typer import Option

class LoginModel(BaseModel):
    username: str
    password: str


class RegisterModel(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    username: str
    password: str

class OrderModel(BaseModel):
    id: int
    product_id: int
    user_id: int
    count: int
    order_status: str

class CategoryModel(BaseModel):
    id: int
    name: str

class ProductModel(BaseModel):
    id: int
    name: str
    description: str
    count: int
    price: float

class JWTModel(BaseModel):
    authjwt_secret_key: str ='c1f4536c33cdb2bbb64229c815dc46a2f949f51a1dee78d991ad3eb961b9d068'