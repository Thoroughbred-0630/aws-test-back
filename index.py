
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import sample

router = APIRouter()

app = FastAPI(
    title="The API server for AWS Test Application",
    dscription="The API Server for AWS Test Application",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(sample.router, prefix="/api/v1/sample", tags=["sample"])