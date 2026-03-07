from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserResponse,UserLogin
from app.services.user_service import get_user_by_email, create_user, authenticate_user,store_refresh_token
from app.core.security import create_access_token, create_refresh_token, decode_token
from app.core.deps import get_db
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = create_user(db, user)

    return new_user


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    db_user = authenticate_user(db, form_data.username, form_data.password)

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        data={"sub": db_user.email}
    )

    refresh_token = create_refresh_token(
    data={"sub": db_user.email}
)

    store_refresh_token(
    db=db,
    user_id=db_user.id,
    token=refresh_token
)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }
    
@router.post("/refresh")
def refresh_token(refresh_token: str):

    payload = decode_token(refresh_token)

    email = payload.get("sub")

    if email is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token"
        )

    new_access_token = create_access_token(
        data={"sub": email}
    )

    return {
        "access_token": new_access_token,
        "token_type": "bearer"
    }