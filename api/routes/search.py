from fastapi import APIRouter

from api.schemas import (
    TextSearchRequest,
    SearchResponse,
)

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.post("/text", response_model=SearchResponse)
def search_text(request: TextSearchRequest):

    return SearchResponse(
        query=request.query,
        results=[]
    )

