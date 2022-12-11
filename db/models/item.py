from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from db.db_context import Base

class Item(Base):
    __tablename__ = "items"
    item_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    sku = Column(String)
    price = Column(Float)
    category = Column(String)
    orders = relationship("Order", back_populates="item")
