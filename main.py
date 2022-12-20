from personal_admon_backend.orm.database import engine, Base
from personal_admon_backend.orm.models import *


def init_db():

    Base.metadata.create_all(engine, checkfirst=True)

    print("Initialized the db")


if __name__ == "__main__":
    init_db()
