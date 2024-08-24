from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from datetime import datetime
import models, schemas


# Get a book by its ID
def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.book_id == book_id).first()


# Get a book by its unique ID
def get_book_by_unique_id(db: Session, book_unique_id: str):
    return db.query(models.Book).filter(models.Book.book_unique_id == book_unique_id).first()


# Get a list of books
def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()


# Create a new book
def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


# Update a book by its ID
def update_book(db: Session, book_id: int, book: schemas.BookCreate):
    db_book = db.query(models.Book).filter(models.Book.book_id == book_id).first()
    if db_book:
        db_book.book_name = book.book_name
        db_book.book_author = book.book_author
        db.commit()
        db.refresh(db_book)
        return db_book
    else:
        return None


# Delete a book by its ID
def delete_book(db: Session, book_id: int):
    db_book = db.query(models.Book).filter(models.Book.book_id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
        return True
    else:
        return False


# Get a student by its ID
def get_student_by_id(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.student_id == student_id).first()


# Get a student by its ID card number
def get_student_by_id_card_number(db: Session, student_id_card_number: str):
    return db.query(models.Student).filter(models.Student.student_id_card_number == student_id_card_number).first()


# Get a list of students
def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()


# Create a new student
def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


# Update a student by its ID
def update_student(db: Session, student_id: int, student: schemas.StudentCreate):
    db_student = db.query(models.Student).filter(models.Student.student_id == student_id).first()
    if db_student:
        db_student.student_name = student.student_name
        db_student.student_email = student.student_email
        db.commit()
        db.refresh(db_student)
        return db_student
    else:
        return None


# Delete a student by its ID
def delete_student(db: Session, student_id: int):
    db_student = db.query(models.Student).filter(models.Student.student_id == student_id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
        return True
    else:
        return False


# Get an inventory entry by its ID
def get_inventory_by_id(db: Session, inventory_id: int):
    return db.query(models.Inventory).filter(models.Inventory.inventory_id == inventory_id).first()


# Get an inventory entry by the book's unique ID
def get_inventory_by_book_unique_id(db: Session, book_unique_id: str):
    return db.query(models.Inventory).filter(models.Inventory.book_unique_id == book_unique_id).first()


# Get a list of inventory entries
def get_inventories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Inventory).offset(skip).limit(limit).all()


# Create a new inventory entry
def create_inventory(db: Session, inventory: schemas.InventoryCreate):
    db_book = get_book_by_unique_id(db=db, book_unique_id=inventory.book_unique_id)
    if db_book is None:
        return None 
    db_inventory = models.Inventory(**inventory.dict())
    db.add(db_inventory)
    db.commit()
    db.refresh(db_inventory)
    return db_inventory


# Update an inventory entry by its ID
def update_inventory(db: Session, inventory_id: int, inventory: schemas.InventoryCreate):
    db_inventory = db.query(models.Inventory).filter(models.Inventory.inventory_id == inventory_id).first()
    if db_inventory:
        db_inventory.no_of_book_copies = inventory.no_of_book_copies
        db.commit()
        db.refresh(db_inventory)
        return db_inventory
    else:
        return None


# Delete an inventory entry by its ID
def delete_inventory(db: Session, inventory_id: int):
    db_inventory = db.query(models.Inventory).filter(models.Inventory.inventory_id == inventory_id).first()
    if db_inventory:
        db.delete(db_inventory)
        db.commit()
        return True
    else:
        return False


# Get a book issue transaction by its ID
def get_transaction_issue_by_id(db: Session, transaction_issue_id: int):
    return db.query(models.TransactionIssue).filter(models.TransactionIssue.transaction_issue_id == transaction_issue_id).first()


# Get a list of book issue transactions
def get_transaction_issues(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TransactionIssue).offset(skip).limit(limit).all()


# Create a new book issue transaction
def create_transaction_issue(db: Session, transaction_issue: schemas.TransactionIssueCreate):
    db_transaction_issue = models.TransactionIssue(**transaction_issue.dict())
    db.add(db_transaction_issue)
    db.commit()
    db.refresh(db_transaction_issue)
    return db_transaction_issue


# Delete a book issue transaction by its ID
def delete_transaction_issue(db: Session, transaction_issue_id: int):
    db_transaction_issue = db.query(models.TransactionIssue).filter(models.TransactionIssue.transaction_issue_id == transaction_issue_id).first()
    if db_transaction_issue:
        db.delete(db_transaction_issue)
        db.commit()
        return True
    else:
        return False


# Get a book return transaction by its ID
def get_transaction_return_by_id(db: Session, transaction_return_id: int):
    return db.query(models.TransactionReturn).filter(models.TransactionReturn.transaction_return_id == transaction_return_id).first()


# Get a list of book return transactions
def get_transaction_returns(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TransactionReturn).offset(skip).limit(limit).all()


# Create a new book return transaction
def create_transaction_return(db: Session, transaction_return: schemas.TransactionReturnCreate):
    db_transaction_return = models.TransactionReturn(**transaction_return.dict())
    db.add(db_transaction_return)
    db.commit()
    db.refresh(db_transaction_return)
    return db_transaction_return


# Delete a book return transaction by its ID
def delete_transaction_return(db: Session, transaction_return_id: int):
    db_transaction_return = db.query(models.TransactionReturn).filter(models.TransactionReturn.transaction_return_id == transaction_return_id).first()
    if db_transaction_return:
        db.delete(db_transaction_return)
        db.commit()
        return True
    else:
        return False


# Get a list of the most popular books (based on issue count)
def get_popular_books(db: Session, limit: int = 5):
    return (db.query(models.Book.book_unique_id, models.Book.book_name, func.count(models.TransactionIssue.book_unique_id).label("issue_count")).join(models.TransactionIssue, models.Book.book_unique_id == models.TransactionIssue.book_unique_id).group_by(models.Book.book_unique_id, models.Book.book_name).order_by(desc("issue_count")).limit(limit).all())