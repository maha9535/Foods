from sqlalchemy import Column, Integer, String
from Database.database import Base



class Restaurants(Base):
    __tablename__ = "Users"


    id = Column(Integer, primary_key=True)
    cust_name = Column(String)
    contact_no= Column(String)
    email = Column(String)
    location = Column(String)