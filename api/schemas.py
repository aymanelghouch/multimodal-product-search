from pydantic import BaseModel, Field

class TextSearchRequest(BaseModel):
    query: str = Field(
        ...,
        min_length=1,
        description="The text query for searching products."
                       )

    top_k: int = Field(
        default=5,
        ge=1,
        le=1000,
        description="The number of top results to return."
    )

class ProductResult(BaseModel):
    product_id: str 
    score: float


class SearchResponse(BaseModel):
    query: str
    results: list[ProductResult]