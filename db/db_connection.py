from sqlalchemy import create_engine
import db.db_context, db.models.customer, db.models.product, db.models.order
from db.db_context import Base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///name.bd", echo=True)


def create_tables(engine):
    Base.metadata.create_all(bind=engine)


