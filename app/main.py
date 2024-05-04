from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import users

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the router in the main app
app.include_router(users.router)
