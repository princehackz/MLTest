from sqlalchemy import Column,Integer,String,DateTime
from database import Base
from datetime import datetime
class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    username=Column(String)
    password=Column(String)
    role=Column(String,default="Client")
class Document(Base):
    __tablename__="documents"
    document_id=Column(Integer,primary_key=True)
    title=Column(String)
    company_name=Column(String)
    document_type=Column(String)
    uploaded_by=Column(String)
    file_path=Column(String)
    created_at=Column(DateTime,default=datetime.now)
