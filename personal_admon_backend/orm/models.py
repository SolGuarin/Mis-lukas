from sqlalchemy import Column, Integer, String, Float, BigInteger, Boolean, ForeignKey
from sqlalchemy.dialects import postgresql
from personal_admon_backend.orm.database import Base
from sqlalchemy.orm import relationship


class Account(Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    type = Column(String)
    note = Column(String)


class Movement(Base):
    __tablename__ = "movement"

    id = Column(Integer, primary_key=True, autoincrement=True)
    account_id = Column(BigInteger, ForeignKey("account.id"))
    account = relationship("Account", foreign_keys=[account_id])
    category_id = Column(BigInteger, ForeignKey("category.id"))
    category = relationship("Category", foreign_keys=[category_id])
    amount = Column(Float)
    note = Column(String)
    description = Column(String)
    from_account_id = Column(Integer)
    to_account_id = Column(Integer)
    type = Column(String)
    date = Column(String)


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    type = Column(String)


class MovementTransactionLink(Base):
    __tablename__ = "movement_transaction_link"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    movement_id = Column(Integer)
    debit_transaction_uid = Column(postgresql.UUID)
    credit_transaction_uid = Column(postgresql.UUID)
    investment_uid = Column(postgresql.UUID)
    backward_transaction_uid = Column(postgresql.UUID)


class DebitTransaction(Base):
    __tablename__ = "debit_transaction"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(postgresql.UUID(as_uuid=True), primary_key=True)
    date = Column(String)
    description = Column(String)
    value = Column(Float)
    account = Column(String)
    repetition = Column(Integer)
    branch_office = Column(String)
    discount = Column(Float)
    balance = Column(Float)
    source_file = Column(String)
    reference = Column(String)
    document = Column(String)
    office = Column(String)
    source = Column(String)


class CreditTransaction(Base):
    __tablename__ = "credit_transaction"

    id = Column(Integer)
    uid = Column(postgresql.UUID(as_uuid=True), primary_key=True)
    nro_authorization = Column(String)
    transaction_date = Column(String)
    description = Column(String)
    original_value = Column(Float)
    currency = Column(String)
    repetition = Column(BigInteger)
    is_temporal = Column(Boolean)


class CreditTransactionList(Base):
    __tablename__ = "credit_transaction_list"

    credit_transaction_uid = Column(postgresql.UUID(as_uuid=True), primary_key=True)
    agreed_rate = Column(Float)
    ea_billed_rate = Column(Float)
    charges_and_pay_off = Column(Float)
    balance_to_be_differed = Column(Float)
    installment = Column(Integer)
    nro_installment = Column(Integer)
    source = Column(String)


class ExchangeCurrency(Base):
    __tablename__ = "exchange_currency"
    id = Column(Integer, primary_key=True, autoincrement=True)
    value_source = Column(String)
    currency_source = Column(String)
    value_destinity = Column(String)
    currency_destinity = Column(String)


