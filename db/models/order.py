import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from db.db_context import Base

class Order(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    sum = Column(Integer)
    #customer_id = 
    #item_id = 