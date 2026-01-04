from fastapi import FastAPI
from router.profile import profile_router
from router.projects import projects_router

app = FastAPI(
    title="Aliya Firdous Portfolio API",
    description="A personal portfolio API showcasing my profile, skills, and projects.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/")
def root():
    """
    Root endpoint for the portfolio API.
    """
    return {
        "message": "hello! Welcome to Aliya Firdous's Portfolio API."
    }

app.include_router(profile_router)
app.include_router(projects_router)
