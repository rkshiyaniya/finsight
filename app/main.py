from fastapi import FastAPI
from app.api.routes import router as api_router
from app.api.auth import router as auth_router

app = FastAPI(title="FinSight", description="A FinTech Transaction Analyzer", version="0.1.0")

@app.get("/health", tags=["System"])
def health_check():
    return {"status": "ok"}

# include more routes later
app.include_router(api_router)
app.include_router(auth_router) 