from pydantic import BaseModel

class User_Schema(BaseModel):
    cust_name: str
    contact_no: str
    email: str
    location: str