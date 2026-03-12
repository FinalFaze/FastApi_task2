from fastapi import FastAPI
from app.routers.blog import router as blog_router

app = FastAPI(title="Blogicum API", version="0.2.0")

app.include_router(blog_router, prefix="/api/v1", tags=["blog"])

@app.get("/api/v1/health")
def health():
    return {"status": "ok"}
