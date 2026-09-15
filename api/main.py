from fastapi import FastAPI
from api.routes.search import router as search_router




app = FastAPI(
    title='Multimodal Product Search API',
    description='API for text, image and multimodal product search.',
    version='0.1.0',
)



@app.get('/health')
def health_check():
    return {
        "status": "ok"
    }


app.include_router(search_router)