from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)# Initialize database and create tables if they don't exist

app = FastAPI()# Create the FastAPI app


# Dependency function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create a new book
@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.create_book(db=db, book=book)
    return db_book


# Create a new student
@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = crud.create_student(db=db, student=student)
    return db_student


# Create a new inventory entry
@app.post("/inventory/", response_model=schemas.Inventory)
def create_inventory(inventory: schemas.InventoryCreate, db: Session = Depends(get_db)):
    db_inventory = crud.create_inventory(db=db, inventory=inventory)
    if db_inventory is None:
        raise HTTPException(status_code=400, detail="Book ID not found")
    return db_inventory


# Update an existing inventory entry
@app.put("/inventory/{inventory_id}", response_model=schemas.Inventory)
def update_inventory(inventory_id: int, inventory: schemas.InventoryCreate, db: Session = Depends(get_db)):
    db_inventory = crud.update_inventory(db=db, inventory_id=inventory_id, inventory=inventory)
    if db_inventory is None:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return db_inventory


# Create a new book issue transaction
@app.post("/transaction_issue/", response_model=schemas.TransactionIssue)
def create_transaction_issue(transaction_issue: schemas.TransactionIssueCreate, db: Session = Depends(get_db)):
    # Check if book is available
    db_inventory = crud.get_inventory_by_book_unique_id(db=db, book_unique_id=transaction_issue.book_unique_id)
    if db_inventory is None or db_inventory.no_of_book_copies == 0:
        raise HTTPException(status_code=400, detail="Book is not available in the library")

    # Check if student can borrow another book
    db_student = crud.get_student_by_id_card_number(db=db, student_id_card_number=transaction_issue.student_id_card_number)
    try:
        # Update student book count before proceeding
        db_student.no_of_books_holding += 1
        # This will raise ValueError if maximum limit is crossed
        schemas.Student.validate_no_of_books_holding(db_student.no_of_books_holding) 
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) 

    # Create transaction issue
    db_transaction_issue = crud.create_transaction_issue(db=db, transaction_issue=transaction_issue)

    # Update inventory
    db_inventory.no_of_book_copies -= 1
    db.commit()

    # Update student
    db.commit()
    return db_transaction_issue


# Create a new book return transaction
@app.post("/transaction_return/", response_model=schemas.TransactionReturn)
def create_transaction_return(transaction_return: schemas.TransactionReturnCreate, db: Session = Depends(get_db)):
    db_transaction_return = crud.create_transaction_return(db=db, transaction_return=transaction_return)
    # Update inventory
    db_inventory = crud.get_inventory_by_book_unique_id(db=db, book_unique_id=transaction_return.book_unique_id)
    db_inventory.no_of_book_copies += 1
    db.commit()
    # Update student
    db_student = crud.get_student_by_id_card_number(db=db, student_id_card_number=transaction_return.student_id_card_number)
    db_student.no_of_books_holding -= 1
    db.commit()
    return db_transaction_return


# Get a list of the most popular books
@app.get("/popular_books/", response_model=List[schemas.PopularBook])
def get_popular_books(db: Session = Depends(get_db)):
    return  crud.get_popular_books(db)