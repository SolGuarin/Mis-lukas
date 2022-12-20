from sqlalchemy.orm import Session

from personal_admon_backend.orm import models
from personal_admon_backend.orm.schemas import *


def get_usuario(db: Session, usuario_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()


def create_usuario(db: Session, usuario: UsuariosCreateSchema):
    db_item = models.Usuario(**usuario.dict())
    db.add(db_item)
    db.commit()
    return db_item


def update_usuario(db: Session, usuario: UsuariosSchema):
    db.query(models.Usuario).filter(models.Usuario.id == usuario.id).update(usuario.dict())
    db.commit()


def delete_usuario(db: Session, usuario_id: int):
    db_item = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    db.delete(db_item)
    db.commit()

# crud Movement


def create_movement(db: Session, movement: MovementCreateSchema):
    db_item = models.Movement(**movement.dict())
    db.add(db_item)
    db.commit()
    return db_item

