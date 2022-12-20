# FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import HTTPException
from fastapi import Body, Path
from personal_admon_backend.orm.schemas import UsuariosSchema, UsuariosCreateSchema, CategoriasSchema, \
    PostsCreateSchema, PostsSchema
from personal_admon_backend.crud import crud_usuarios, crud_categorias, crud_posts
from personal_admon_backend.orm.database import *

from sqlalchemy.orm import Session
from starlette import status

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# endpoints de usuarios


@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=["Home"]
)
def home():
    return {"input": "it´s working..."}


@app.post(
    path="/usuarios",
    status_code=status.HTTP_201_CREATED,  # porque es para crear una persona
    tags=["usuarios"],
    summary="create usuario in the app"
)
def create_usuario(usuario: UsuariosCreateSchema = Body(...)):
    """
    Create User

    This path operation creates a user in the app and save the information in the database

    Parameters:
        -Request body parameter:
            -**usuario: UsuariosCreateSchema** -> A usuario model with login, password, nickname and email
    """
    crud_usuarios.create_usuario(usuario=usuario.dict())


@app.get(
    path="/usuarios/{usuario_id}",
    status_code=status.HTTP_200_OK,
    response_model=UsuariosSchema,
    tags=["usuarios"]
)
def show_usuario(
        usuario_id: int = Path(
            ...,
            title="Usuario Id",
            description="This is Usuario Id. It´s required",
            example=123
        )
):
    """
    Show User

    This path operation show a user in the in the app

    Parameters:
    - usuario_id: int

    Returns a UserSchema model with id, login, password, nickname and email
    """
    usuario: dict = crud_usuarios.read_usuario(usuario_id=usuario_id)
    if usuario:
        return usuario
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This person doesn't exist"
        )


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
    crud_usuarios.delete_usuario(usuario_id=usuario_id)
    return "Se eliminó exitosamente"


@app.put(
    path="/usuarios",
    status_code=status.HTTP_200_OK,  # porque es para crear una persona
    tags=["usuarios"],
    summary="update usuario in the app"
)
def update_usuario(usuario: UsuariosSchema = Body(...)):
    """
    Soleny your homework is to fill up the documentation
    """
    crud_usuarios.update_usuario(usuario=usuario.dict())

# endpoints de categorías


@app.post(
    path="/categorias",
    status_code=status.HTTP_201_CREATED,
    tags=["categorias"],
    response_model=CategoriasSchema,
    summary="create category in the app"
)
def create_categoria(categoria: CategoriasSchema = Body(...)):
    """
    Soleny your homework is to fill up the documentation
    """
    crud_categorias.create_categoria(nombre_categoria=categoria.nombre_categoria)
    return categoria


@app.get(
    path="/categorias/{categoria_id}",
    status_code=status.HTTP_200_OK,
    response_model=CategoriasSchema,
    tags=["categorias"]
)
def show_categoria(
        categoria_id: int = Path(
            ...,
            title="Categoria Id",
            description="This is Categoria Id. It´s required",
        )
):
    categoria: dict = crud_categorias.read_categoria(categoria_id=categoria_id)
    if categoria:
        return categoria
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This categoria doesn't exist"
        )


@app.delete(
    path="/categorias/{categoria_id}",
    status_code=status.HTTP_200_OK,
    tags=["categorias"]
)
def delete_categoria(
        categoria_id: int = Path(
            ...,
            title="categoria_id",
            description="This is categoria Id. It´s required",
        )
):
    crud_categorias.delete_categoria(categoria_id=categoria_id)
    return "La categoria se eliminó exitosamente"


@app.put(
    path="/categorias",
    status_code=status.HTTP_200_OK,
    tags=["categorias"],
    response_model=CategoriasSchema,
    summary="update category in the app"
)
def update_categoria(categoria: CategoriasSchema = Body(...)):
    """
    Soleny your homework is to fill up the documentation
    """
    crud_categorias.update_categoria(nombre_categoria=categoria.nombre_categoria, categoria_id=categoria.id)
    return categoria

# endpoint de posts

@app.post(
    path="/posts",
    status_code=status.HTTP_201_CREATED,  # porque es para crear una persona
    response_model=PostsCreateSchema,
    tags=["posts"],
    summary="create post in the app"
)
def create_post(post: PostsCreateSchema = Body(...)):
    """
    Soleny your homework is to fill up the documentation
    """
    crud_posts.create_post(post=post.dict())

    return post


@app.get(
    path="/posts/{post_id}",
    status_code=status.HTTP_200_OK,
    response_model=PostsSchema,
    tags=["posts"]
)
def show_post(
        post_id: int = Path(
            ...,
            title="Post Id",
            description="This is post Id. It´s required",
        )
):
    post: dict = crud_posts.read_post(post_id=post_id)
    if post:
        return post
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This post doesn't exist"
        )


@app.delete(
    path="/posts/{post_id}",
    status_code=status.HTTP_200_OK,
    tags=["posts"]
)
def delete_post(
        post_id: int = Path(
            ...,
            title="post_id",
            description="This is post Id. It´s required",
        )
):
    crud_posts.delete_post(post_id=post_id)
    return "Se eliminó exitosamente el post"


@app.put(
    path="/posts",
    status_code=status.HTTP_200_OK,  # porque es para crear una persona
    response_model=PostsSchema,
    tags=["posts"],
    summary="update post in the app"
)
def update_post(post: PostsSchema = Body(...)):
    """
    Soleny your homework is to fill up the documentation
    """
    crud_posts.update_post(post=post.dict())

    return post
