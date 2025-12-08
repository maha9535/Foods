from sqlalchemy import Column, Integer, String, Boolean
from Database.database import Base


class Foods(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True)
    food_name = Column(String)
    price = Column(Integer)
    qty = Column(Integer)
    availability = Column(Boolean)