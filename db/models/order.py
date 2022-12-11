import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from db.db_context import Base

class Order(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    quantity =  Column(Integer)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    customer = relationship("Customer", back_populates="orders")
    product_id = Column(Integer, ForeignKey("products.product_id"))
    product = relationship("Product", back_populates="orders")
