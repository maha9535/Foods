from sqlalchemy import Column, Integer, String
from Database.database import Base



class Restaurants(Base):
    __tablename__ = "restaurants"


    id = Column(Integer, primary_key=True)
    rest_name = Column(String)
    location = Column(String)
    contact_person = Column(String)
    phone = Column(String)