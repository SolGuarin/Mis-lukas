from fastapi import Depends, FastAPI, HTTPException, Body, Path
from sqlalchemy.orm import Session
from starlette import status

from personal_admon_backend.orm import crud, schemas
from personal_admon_backend.orm.database import SessionLocal

from personal_admon_backend.orm.schemas import *

app = FastAPI()
@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=["Home"]
)
def home():
    return {"personal finance"}

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# end points de usuarios


@app.get("/usuarios/{usuario_id}", response_model=schemas.UsuariosSchema)
def read_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = crud.get_usuario(db, usuario_id=usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_usuario


@app.post(
    path="/usuarios",
    status_code=status.HTTP_201_CREATED,  # porque es para crear una persona
    tags=["usuarios"],
    summary="create usuario in the app"
)
def create_usuario(usuario: UsuariosCreateSchema = Body(...), db: Session = Depends(get_db)):
    """
    Create User

    This path operation creates a user in the app and save the information in the database

    Parameters:
        -Request body parameter:
            -**usuario: UsuariosCreateSchema** -> A usuario model with login, password, nickname and email
    """
    crud.create_usuario(db=db, usuario=usuario)


@app.put(
    path="/usuarios",
    status_code=status.HTTP_200_OK,  # porque es para crear una persona
    tags=["usuarios"],
    summary="update usuario in the app"
)
def update_usuario(usuario: UsuariosSchema = Body(...),  db: Session = Depends(get_db)):
    """
    Soleny your homework is to fill up the documentation
    """
    crud.update_usuario(db=db, usuario=usuario)


@app.delete(
    path="/usuarios/{usuario_id}",
    status_code=status.HTTP_200_OK,
    tags=["usuarios"]
)
def delete_usuario(
        usuario_id: int = Path(
            ...,
            title="usuario_id",
            description="This is Usuario Id. It´s required",
        )
):
    crud.delete_usuario(db=SessionLocal, usuario_id=usuario_id)
    return "Se eliminó exitosamente"

# endpoints de movements

@app.post(
    path="/usuarios",
    status_code=status.HTTP_201_CREATED,  # porque es para crear una persona
    tags=["movements"],
    summary="create usuario in the app"
)
def create_movement(movement: MovementCreateSchema = Body(...), db: Session = Depends(get_db)):
    """
    Create Movement

    This path operation creates a user in the app and save the information in the database

    Parameters:
        -Request body parameter:
            -**usuario: UsuariosCreateSchema** -> A usuario model with login, password, nickname and email
    """
    crud.create_movement(db=db, movement=movement)
