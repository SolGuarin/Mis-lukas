from sqlalchemy.orm import Session

from personal_admon_backend.orm import models
from personal_admon_backend.orm.schemas import *


# crud Movement


def create_movement(db: Session, movement: MovementCreateSchema):
    db_item = models.Movement(**movement.dict())
    db.add(db_item)
    db.commit()
    return db_item


def get_movement(db: Session, movement_id: int):
    return db.query(models.Movement).filter(models.Movement.id == movement_id).first()


def get_all_movement(db: Session):
    return db.query(models.Movement).filter().all()


# crud category


def create_category(db: Session, category: CategoryCreateSchema):
    db_item = models.Category(**category.dict())
    db.add(db_item)
    db.commit()
    return db_item


def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()


def get_all_category(db: Session):
    return db.query(models.Category).filter().all()


# crud account
def get_account(db: Session, account_id: int):
    return db.query(models.Account).filter(models.Account.id == account_id).first()


def create_account(db: Session, account: AccountCreateSchema):
    db_item = models.Account(**account.dict())
    db.add(db_item)
    db.commit()
    return db_item


def get_all_account(db: Session):
    return db.query(models.Account).filter().all()


# crud debit transaction
def get_debit_transaction(db: Session, debit_transaction_id: int):
    return db.query(models.DebitTransaction).filter(models.DebitTransaction.id == debit_transaction_id).first()


def get_all_debit_transaction(db: Session):
    return db.query(models.DebitTransaction).filter().all()


# crud credit transaction
def get_credit_transaction(db: Session, credit_transaction_id: int):
    return db.query(models.CreditTransaction).filter(models.CreditTransaction.id == credit_transaction_id).first()


def get_all_credit_transaction(db: Session):
    return db.query(models.CreditTransaction).filter().all()
