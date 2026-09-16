from fastapi import APIRouter

from api.schemas import (
    TextSearchRequest,
    ImageSearchRequest,
    MultimodalSearchRequest,
    SearchResponse,
)

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)



@router.post("/text", response_model=SearchResponse)
def search_text(request: TextSearchRequest):
    return SearchResponse(
        results=[],
        total=0,
    )

@router.post("/image    ", response_model=SearchResponse)
def search_image(request: ImageSearchRequest):
    return SearchResponse(
        results=[],
        total=0,
    )



@router.post("/multimodal", response_model=SearchResponse)
def search_multimodal(request: MultimodalSearchRequest):
    return SearchResponse(
        results=[],
        total=0,
    )

