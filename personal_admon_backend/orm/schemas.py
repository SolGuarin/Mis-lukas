from uuid import UUID
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class AccountGetSchema(BaseModel):
    id: int = Field()
    name: str = Field()
    type: str = Field()
    note: str = Field()

    class Config:
        orm_mode = True


class CategoryGetSchema(BaseModel):
    id: int = Field()
    name: str = Field()
    type: str = Field()

    class Config:
        orm_mode = True


class MovementCreateSchema(BaseModel):
    account_id: Optional[int] = Field()
    category_id: Optional[int] = Field()
    amount: Optional[float] = Field()
    note: Optional[str] = Field()
    description: Optional[str] = Field()
    from_account_id: Optional[int] = Field()
    to_account_id: Optional[int] = Field()
    type: Optional[str] = Field()
    date: Optional[str] = Field()

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
    account: AccountGetSchema
    category: CategoryGetSchema

    class Config:
        orm_mode = True


# schema category

class CategoryCreateSchema(BaseModel):
    name: str = Field()
    type: str = Field()

    class Config:
        orm_mode = True


# schema account
class AccountCreateSchema(BaseModel):
    name: str = Field()
    type: str = Field()
    note: str = Field()


# schema Debit Transaction
class DebitTransactionGetSchema(BaseModel):
    id: int = Field()
    uid: UUID = Field()
    date: Optional[str] = Field()
    description: Optional[str] = Field()
    value: Optional[float] = Field()
    account: Optional[str] = Field()
    repetition: Optional[int] = Field()
    branch_office: Optional[str] = Field()
    discount: Optional[float] = Field()
    balance: Optional[float] = Field()
    source_file: Optional[str] = Field()
    reference: Optional[str] = Field()
    document: Optional[str] = Field()
    office: Optional[str] = Field()
    source: Optional[str] = Field()

    class Config:
        orm_mode = True



