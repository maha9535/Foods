from Database.database import SessionLocal

def connect_to_db():
    db = SessionLocal()
    try:
        print("Connected to DB")
        yield db
    finally:

        db.close()