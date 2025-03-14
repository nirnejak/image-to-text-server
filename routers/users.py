from fastapi import APIRouter

router = APIRouter()

users = [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/", tags=["users"])
async def read_users():
    return users


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "currentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
