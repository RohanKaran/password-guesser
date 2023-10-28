from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import api
from app.models import init_models


def create_app():
    app = FastAPI(
        title="Password Guesser",
        version="0.0.1",
        description="Guess the password using OpenAI's GPT-3",
        debug=True,
    )

    app.include_router(api)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allows CORS from this origin
        allow_credentials=True,
        allow_methods=["*"],  # Allows all methods
        allow_headers=["*"],  # Allows all headers
    )

    @app.on_event("startup")
    async def startup():
        await init_models()

    return app
