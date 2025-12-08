from fastapi import FastAPI
from Database.database import Base, engine
# routers -> foods router import
# step-1
from routers.food import food_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
# step -2
# decorator function
@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(food_router)