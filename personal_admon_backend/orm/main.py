from fastapi import Depends, FastAPI, HTTPException, Body, Path
from sqlalchemy.orm import Session
# from sqlalchemy.testing import db
from starlette import status
from personal_admon_backend.orm import crud
from personal_admon_backend.orm.database import SessionLocal
from personal_admon_backend.orm.schemas import *
from personal_admon_backend.orm.models import *
from uuid import UUID

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

# endpoints de movements
# # create movement
@app.post(
    path="/movements",
    status_code=status.HTTP_201_CREATED,  # porque es para crear una persona
    tags=["movements"],
    summary="create movement in the app",
    response_model=MovementGetSchema
)
def create_movement(movement: MovementCreateSchema = Body(...), db: Session = Depends(get_db)):
    """
    Create Movement

    This path operation creates a user in the app and save the information in the database

    Parameters:
        -Request body parameter:
            -**usuario: UsuariosCreateSchema** -> A usuario model with login, password, nickname and email
    """
    # Common Property
    if movement.amount <= 0:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail='Amount negative not allowed',
        )

    # Property based on the type

    if movement.type == 'Expenses':
        # Mis validations
        exist_account = crud.get_account(db=db, account_id=movement.account_id) is not None
        exist_category = crud.get_category(db=db, category_id=movement.category_id) is not None

        if exist_account and exist_category:
            movement = crud.create_movement(db=db, movement=movement)
            return movement
        else:
            raise HTTPException(
                status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
                detail='Account Id or Category was not found in the db',
            )

    elif movement.type == 'Transfer':
        # Mis validations
        pass

    elif movement.type == 'Income':
        # Mis validations
        pass

    else:
        pass

    crud.create_movement(db=db, movement=movement)


# # get a movement
@app.get(
    path="/movements/{movement_id}",
    status_code=status.HTTP_200_OK,
    response_model=MovementGetSchema,
    tags=["movements"]
)
def show_movement(
        movement_id: int = Path(
            ...,
            title="Movement Id",
            description="This is Movement Id. It??s required",
            example=12
        ),
        db: Session = Depends(get_db)
):
    """
    Show Movement

    This path operation show a user the in the app

    Parameters:
    - usuario_id: int

    Returns a UserSchema model with id, login, password, nickname and email
    """
    movement = crud.get_movement(db=db, movement_id=movement_id)
    if movement:
        return movement
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This movement doesn't exist"
        )

# # get all movement
@app.get(
    path="/movements",
    status_code=status.HTTP_200_OK,
    response_model=list[MovementGetSchema],
    tags=["movements"]
)
def show_all_movement(
        db: Session = Depends(get_db)
):
    """
    Show all Movement

    This path operation show a user the in the app

    Parameters:
    - usuario_id: int

    Returns a UserSchema model with id, login, password, nickname and email
    """
    movement = crud.get_all_movement(db=db)
    return movement


# endpoints category

@app.post(
    path="/categories",
    status_code=status.HTTP_201_CREATED,  # porque es para crear una persona
    tags=["categories"],
    summary="create category in the app",
    response_model=CategoryGetSchema
)
def create_category(category: CategoryCreateSchema = Body(...), db: Session = Depends(get_db)):
    """
    Create Movement

    This path operation creates a user in the app and save the information in the database

    Parameters:
        -Request body parameter:
            -**usuario: UsuariosCreateSchema** -> A usuario model with login, password, nickname and email
    """
    category = crud.create_category(db=db, category=category)
    return category


# # get category
@app.get(
    path="/categories/{category_id}",
    status_code=status.HTTP_200_OK,
    response_model=CategoryGetSchema,
    tags=["categories"]
)
def show_category(
        category_id: int = Path(
            ...,
            title="Category Id",
            description="This is Category Id. It??s required",
            example=123
        ),
        db: Session = Depends(get_db)
):
    """
    Show Category

    This path operation show a user the in the app

    Parameters:
    - usuario_id: int

    Returns a UserSchema model with id, login, password, nickname and email
    """
    category = crud.get_category(db=db, category_id=category_id)
    if category:
        return category
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This category doesn't exist"
        )

# # get all category
@app.get(
    path="/categories",
    status_code=status.HTTP_200_OK,
    response_model=list[CategoryGetSchema],
    tags=["categories"]
)
def show_all_category(
        db: Session = Depends(get_db)
):
    """
    Show all Category

    This path operation show a user the in the app

    Parameters:
    - usuario_id: int

    Returns a UserSchema model with id, login, password, nickname and email
    """
    category = crud.get_all_category(db=db)
    return category


# endpoints account
# # create account
@app.post(
    path="/accounts",
    status_code=status.HTTP_201_CREATED,  # porque es para crear una persona
    tags=["accounts"],
    summary="create account in the app",
    response_model=AccountGetSchema
)
def create_account(account: AccountCreateSchema = Body(...), db: Session = Depends(get_db)):
    """
    Create Movement

    This path operation creates a user in the app and save the information in the database

    Parameters:
        -Request body parameter:
            -**usuario: UsuariosCreateSchema** -> A usuario model with login, password, nickname and email
    """
    account = crud.create_account(db=db, account=account)
    return account


# # get account

@app.get(
    path="/accounts/{account_id}",
    status_code=status.HTTP_200_OK,
    response_model=AccountGetSchema,
    tags=["accounts"]
)
def show_account(
        account_id: int = Path(
            ...,
            title="Account Id",
            description="This is Account Id. It??s required",
            example=1
        ),
        db: Session = Depends(get_db)
):
    """
    Show Account

    This path operation show a user the in the app

    Parameters:
    - usuario_id: int

    Returns a UserSchema model with id, login, password, nickname and email
    """
    account = crud.get_account(db=db, account_id=account_id)
    if account:
        return account
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This account doesn't exist"
        )

# # get all account
@app.get(
    path="/accounts",
    status_code=status.HTTP_200_OK,
    response_model=list[AccountGetSchema],
    tags=["accounts"]
)
def show_all_account(
        db: Session = Depends(get_db)
):
    """
    Show all Account

    This path operation show a user the in the app

    Parameters:
    - usuario_id: int

    Returns a UserSchema model with id, login, password, nickname and email
    """
    account = crud.get_all_account(db=db)
    return account


# endpoints debit transaction

# # get debit transaction
@app.get(
    path="/debit_transactions/{debit_transaction_uid}",
    status_code=status.HTTP_200_OK,
    response_model=DebitTransactionGetSchema,
    tags=["debit transaction"]
)
def show_debit_transaction(
        debit_transaction_uid: UUID = Path(
            ...,
            title="Debit transaction Id",
            description="This is Debit Transaction Id. It??s required"
        ),
        db: Session = Depends(get_db)
):
    """
    Show Debit Transaction

    This path operation show a user the in the app

    Parameters:
    - usuario_id: int

    Returns a UserSchema model with id, login, password, nickname and email
    """
    debit_transaction = crud.get_debit_transaction(db=db, debit_transaction_uid=debit_transaction_uid)
    if debit_transaction:
        return debit_transaction
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This debit transaction doesn't exist"
        )


# # get all debit transaction
@app.get(
    path="/debit transactions",
    status_code=status.HTTP_200_OK,
    response_model=list[DebitTransactionGetSchema],
    tags=["debit transaction"]
)
def show_all_debit_transaction(
        db: Session = Depends(get_db)
):
    """
    Show all Debit Transaction

    This path operation show a user the in the app

    Parameters:
    - usuario_id: int

    Returns a UserSchema model with id, login, password, nickname and email
    """
    debit_transaction = crud.get_all_debit_transaction(db=db)
    return debit_transaction


# endpoints credit transaction

# # get credit transaction
@app.get(
    path="/credit_transactions/{credit_transaction_uid}",
    status_code=status.HTTP_200_OK,
    response_model=CreditTransactionGetSchema,
    tags=["credit transaction"]
)
def show_credit_transaction(
        credit_transaction_uid: UUID = Path(
            ...,
            title="Credit transaction Id",
            description="This is Credit Transaction Id. It??s required"
        ),
        db: Session = Depends(get_db)
):
    """
    Show Credit Transaction

    This path operation show a user the in the app

    Parameters:
    - usuario_id: int

    Returns a UserSchema model with id, login, password, nickname and email
    """
    credit_transaction = crud.get_credit_transaction(db=db, credit_transaction_uid=credit_transaction_uid)
    if credit_transaction:
        return credit_transaction
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This credit transaction doesn't exist"
        )


# # get all credit transaction
@app.get(
    path="/credit transactions",
    status_code=status.HTTP_200_OK,
    response_model=list[CreditTransactionGetSchema],
    tags=["credit transaction"]
)
def show_all_credit_transaction(
        db: Session = Depends(get_db)
):
    """
    Show all Credit Transaction

    This path operation show a user the in the app

    Parameters:
    - usuario_id: int

    Returns a UserSchema model with id, login, password, nickname and email
    """
    credit_transaction = crud.get_all_credit_transaction(db=db)
    return credit_transaction


# endpoint movement transaction link
@app.post(
    path="/movements_transactions_link",
    status_code=status.HTTP_201_CREATED,  # porque es para crear una persona
    tags=["movement transaction link"],
    summary="create movement transaction link in the app",
    response_model=MovementTransactionLinkCreateSchema
)
def create_movement(movement: MovementTransactionLinkCreateSchema = Body(...), db: Session = Depends(get_db)):
    """
    Create Movement

    This path operation creates a user in the app and save the information in the database

    Parameters:
        -Request body parameter:
            -**usuario: UsuariosCreateSchema** -> A usuario model with login, password, nickname and email
    """
    # Mis validations
    exist_movement = crud.get_movement(db=db, movement_id=movement.movement_id) is not None
    exist_debit_transaction = crud.get_debit_transaction(
        db=db, debit_transaction_uid=movement.debit_transaction_uid) is not None
    exist_credit_transaction = crud.get_credit_transaction(
        db=db, credit_transaction_uid=movement.credit_transaction_uid) is not None

    # print(f'exist_movement: {exist_movement}')
    # print(f'exist_debit_transaction: {exist_debit_transaction}')
    # print(f'exist_credit_transaction: {exist_credit_transaction}')
    # input('yaaaaaaa')

    if exist_movement and (exist_credit_transaction or exist_debit_transaction):
        movement = crud.create_movement_transaction_link(db=db, movement_transaction_link=movement)
        return movement
    else:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail='Movement or Category was not found in the db',
        )
