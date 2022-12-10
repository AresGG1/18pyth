from sqlalchemy import Column, Integer, String, Float
from db.db_context import Base

class Item(Base):
    __tablename__ = "items"
    item_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    sku = Column(String)
    price = Column(Float)
    category = Column(String)

print ("log")