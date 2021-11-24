from ..hashing import gen_salt, hash_pwd
from .. import schemas, models
from fastapi import status, APIRouter
from ..database import Session, get_db
from fastapi import Depends, HTTPException

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse
)
async def create_user(user: schemas.User, db: Session = Depends(get_db)):
    salt = gen_salt()
    user.password = hash_pwd(user.password, salt)
    new_user = models.User(**user.dict(), salt=salt)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=schemas.UserResponse)
async def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id {id} does not exist",
        )
    return user.first()

@router.get("/")
async def get_user(db: Session = Depends(get_db)):
    
    return db.query(models.User).all()