from sqlalchemy import create_engine
import db.db_context, db.models.customer, db.models.item, db.models.order
from db.db_context import Base

engine = create_engine("sqlite:///name.bd", echo=True)

Base.metadata.create_all(bind=engine)
