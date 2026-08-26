# Create Table
from sqlalchemy import Column, Integer, String, Text
from database import Base

# Blog Table
class Blog(Base):
    
    __tablename__ = "blogs"  # Table
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(Text)
    
    