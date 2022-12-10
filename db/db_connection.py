from sqlalchemy import MetaData, create_engine
from sqlalchemy imort sessionmaker;
import db.db_context, db.models.customer, db.models.item 
from db.db_context import Base

#C:\python\sqlLite\sqlite-tools-win32-x86-3400000>sqlite3 ..\..\lab18\db\database.dbC:\python\sqlLite\sqlite-tools-win32-x86-3400000>sqlite3 ..\..\lab18\db\database.db
engine = create_engine("sqlite:///name.bd", echo=True)

Base.metadata.create_all(bind=engine)
print ("log")