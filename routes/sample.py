from fastapi import APIRouter

router = APIRouter()

@router.get("/apiTest")
def test():
    return "success"