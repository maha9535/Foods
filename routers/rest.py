from fastapi import APIRouter, Depends

# schema
from Schemas.rest import Restaurant_Schema
from dependencies import connect_to_db
from sqlalchemy.orm import Session

# database models
from models.rest import Restaurants

Rest_router = APIRouter(prefix="/restaurants", tags=["Restaurants"])

# GET all restaurants
@Rest_router.get("/")
def get_all_restaurants(dbs: Session = Depends(connect_to_db)):
    return dbs.query(Restaurants).all()


# GET restaurant by id
@Rest_router.get("/{rest_id}")
def get_restaurant_by_id(rest_id: int, dbs: Session = Depends(connect_to_db)):
    particular_rest = dbs.query(Restaurants).filter(Restaurants.id == rest_id).first()
    
    if not particular_rest:
        return {"message": "Invalid Id"}
    
    return particular_rest


#post
@Rest_router.post("/")
def create_restaurant(new_rest: Restaurant_Schema, dbs: Session = Depends(connect_to_db)):

   
    name = new_rest.rest_name
    loc = new_rest.location
    contact = new_rest.contact_person
    phone_no = new_rest.phone

   
    new_entry = Restaurants(
        rest_name=name,
        location=loc,
        contact_person=contact,
        phone=phone_no
    )

    # Add to database
    dbs.add(new_entry)
    dbs.commit()
    dbs.refresh(new_entry)

    return new_entry


# PUT 
@Rest_router.put("/{id}")
def update_restaurant(latest_rest: Restaurant_Schema, id: int, dbs: Session = Depends(connect_to_db)):

   
    particular_rest = dbs.query(Restaurants).filter(Restaurants.id == id).first()

    if not particular_rest:
        return {"message": "You have entered an invalid id"}

 
    particular_rest.rest_name = latest_rest.rest_name
    particular_rest.location = latest_rest.location
    particular_rest.contact_person = latest_rest.contact_person
    particular_rest.phone = latest_rest.phone

    
    dbs.commit()
    dbs.refresh(particular_rest)

    
    return particular_rest

# DELETE a restaurant by ID
@Rest_router.delete("/{id}")
def delete_restaurant(id: int, dbs: Session = Depends(connect_to_db)):

    # Find the restaurant
    particular_rest = dbs.query(Restaurants).filter(Restaurants.id == id).first()

    if not particular_rest:
        return {"message": "You have entered an invalid id"}

    # Delete the restaurant
    dbs.delete(particular_rest)
    dbs.commit()

    return {"message": f"Restaurant with id {id} has been deleted successfully"}