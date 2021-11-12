from fastapi import FastAPI
from .database import engine_
from .routers import users, posts, auth, votes
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# # when using alembic, this can be commented out
# models.Base.metadata.create_all(bind=engine_)


app = FastAPI()
# origins = ['https://www.google.com', 'https://www.youtube.com'] # allow access for specific domains
origins = ["*"]  # allow access for all public domains

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # domains that can consume the API
    allow_credentials=True,
    allow_methods=["*"],  # specific http methods to be allowed
    allow_headers=["*"],  # specific request headers to be allowed
)


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)


@app.get("/")
async def hello_world():
    return {"message": "Hello World"}
