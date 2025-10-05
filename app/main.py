from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router
from app.core.config import settings

# Application instance
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    description="Volyzen AI Algorithmic Trading Engine by Jamestall Kadzeya Lab.",
    version="1.0.0",
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Include the main API router
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/healthz", tags=["Health"])
async def health_check():
    """
    Health check endpoint.
    """
    return {"status": "ok", "name": settings.PROJECT_NAME}
