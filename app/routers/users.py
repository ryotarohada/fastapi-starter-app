from fastapi import APIRouter

router = APIRouter()


@router.get("/users")
async def read_users():
    return [{"name": "Ryotaro Hada"}]


@router.get("/users/me")
async def read_user_me():
    return {"name": "Ryotaro Hada"}
