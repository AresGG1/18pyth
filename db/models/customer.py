from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from db.db_context import Base

class Customer(Base):
    __tablename__ = "customers"
    customer_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    age = Column(Integer)
    address = Column(Text)
    orders = relationship("Order", back_populates="customer")
