import uuid

from pydantic import BaseModel
from pydantic import Field


# schema movement

class MovementCreateSchema(BaseModel):
    account_id: int = Field()
    category_id: int = Field()
    amount: float = Field()
    note: str = Field()
    description: str = Field()
    from_account_id: int = Field()
    to_account_id: int = Field()
    type: str = Field()
    date: str = Field()

    class Config:
        orm_mode = True


class MovementGetSchema(BaseModel):
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

    class Config:
        orm_mode = True


# schema category


class CategoryCreateSchema(BaseModel):
    name: str = Field()
    type: str = Field()

    class Config:
        orm_mode = True


class CategoryGetSchema(BaseModel):
    id: int = Field()
    name: str = Field()
    type: str = Field()

    class Config:
        orm_mode = True


# schema account
class AccountCreateSchema(BaseModel):
    name: str = Field()
    type: str = Field()
    note: str = Field()


class AccountGetSchema(BaseModel):
    id: int = Field()
    name: str = Field()
    type: str = Field()
    note: str = Field()

    class Config:
        orm_mode = True


"""
# schema Debit Transaction
class DebitTransactionGetSchema(BaseModel):
    id: int = Field()
    uid: uuid = Field()
    source: str = Field()
"""



