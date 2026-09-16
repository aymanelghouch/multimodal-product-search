from fastapi import APIRouter, HTTPException


router = APIRouter(
    prefix="/products",
    tags=["Products"]

)

@router.get("{product_id}")
def get_product(product_id: str):

    if product_id != "demo":
        raise HTTPException(status_code=404, detail="Product not found")

    return {
        "product_id": product_id,
        "title": "Demo Product",
        "category": "Demo ",
    }

    
