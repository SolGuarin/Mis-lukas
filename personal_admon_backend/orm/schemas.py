from datetime import date
from pydantic import BaseModel
from pydantic import Field


class UsuariosCreateSchema(BaseModel):
    login: str = Field(
        ...,
        min_length=1,
        max_length=25,
        example="juanjosegdoj"
    )
    password: str = Field(
        ...,
        min_length=1,
        max_length=30,
        example="super-secret"
    )
    nickname: str = Field(
        ...,
        min_length=1,
        max_length=30,
        example="juanjosegdoj"
    )
    email: str = Field(
        ...,
        min_length=1,
        max_length=30,
        example="juanjosegdoj@gmail.com"
    )


class UsuariosSchema(UsuariosCreateSchema):
    id: int = Field(
        ...,
        example=1
    )

    class Config:
        orm_mode = True


class CategoriasCreateSchema(BaseModel):
    nombre_categoria: str = Field(
        ...
    )


class CategoriasSchema(CategoriasCreateSchema):
    id: int = Field(
        ...,
    )

    class Config:
        orm_mode = True


class PostsCreateSchema(BaseModel):
    titulo: str = Field(
        ...,
        min_length=1,
        max_length=100,

    )
    fecha_publicacion : date = Field(
        ...
    )
    contenido: str = Field(
        ...,
        min_length=1,
        max_length=5000,
    )
    estatus: str = Field(
        ...
    )
    usuario_id: int = Field(
        ...
    )
    categoria_id: int = Field(
        ...
    )


class PostsSchema (PostsCreateSchema):
    id: int = Field(
        ...
    )

    class Config:
        orm_mode = True

# schema movement


class MovementCreateSchema(BaseModel):
    id: int = Field()
    account_id: int = Field()
    category_id: int = Field()
    amount: float = Field()
    note: str = Field()
    description: str = Field()
    from_account_id: int = Field()
    to_account_id: int = Field()
    type: str = Field()
    date: str = Field()
