from fastapi import APIRouter,Depends, status
from schema import UserCreateRequest
from database import get_db
from fastapi import APIRouter
from sqlalchemy.orm import Session
from service import UserService


router = APIRouter(
    prefix="/user"
)


@router.post("/create",status_code=status.HTTP_201_CREATED)
def create_user(user_request: UserCreateRequest,db: Session = Depends(get_db)):
    service = UserService()
    service.create_user(db, user_request)

@router.get("/list")
def get_all_user(db:Session = Depends(get_db)):
    service = UserService()
    return service.get_all_user(db)

@router.get("/{email}")
def get_user_by_email(email:str, db:Session = Depends(get_db)):
    service = UserService()
    return service.get_user_by_mail(db, email)

@router.delete("/{email}")
def delete_user_by_email(email: str, db:Session = Depends(get_db)):
    service = UserService()
    return service.delete_by_email(db, email)

