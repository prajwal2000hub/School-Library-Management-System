from pydantic import BaseModel, validator
from typing import List, Optional


# Base model for book information
class BookBase(BaseModel):
    book_unique_id: str
    book_name: str
    book_author: str


# Model for creating a new book entry
class BookCreate(BookBase):
    pass


# Model for representing a book with an ID
class Book(BookBase):
    book_id: int

    class Config:
        from_attributes = True


# Base model for student information
class StudentBase(BaseModel):
    student_id_card_number: str
    student_name: str
    student_email: str


# Model for creating a new student entry
class StudentCreate(StudentBase):
    pass


# Model for representing a student with an ID and book holding information
class Student(StudentBase):
    student_id: int
    no_of_books_holding: int = 0


# Validator to ensure no more than 3 books can be held
    @validator('no_of_books_holding', pre=True, always=True)
    def validate_no_of_books_holding(cls, value):
        if value > 3:
            raise ValueError("Maximum limit crossed")
        return value

    class Config:
        from_attributes = True


# Base model for inventory information
class InventoryBase(BaseModel):
    book_unique_id: str
    no_of_book_copies: int


# Model for creating a new inventory entry
class InventoryCreate(InventoryBase):
    pass


# Model for representing an inventory entry with an ID
class Inventory(InventoryBase):
    inventory_id: int

    class Config:
        from_attributes = True


# Base model for book issue transaction information
class TransactionIssueBase(BaseModel):
    student_id_card_number: str
    book_unique_id: str
    issue_date: str


# Model for creating a new book issue transaction entry
class TransactionIssueCreate(TransactionIssueBase):
    pass


# Model for representing a book issue transaction with an ID
class TransactionIssue(TransactionIssueBase):
    transaction_issue_id: int

    class Config:
        from_attributes = True


# Base model for book return transaction information
class TransactionReturnBase(BaseModel):
    student_id_card_number: str
    book_unique_id: str
    return_date: str


# Model for creating a new book return transaction entry
class TransactionReturnCreate(TransactionReturnBase):
    pass


# Model for representing a book return transaction with an ID
class TransactionReturn(TransactionReturnBase):
    transaction_return_id: int

    class Config:
        from_attributes = True


# Model for representing a popular book
class PopularBook(BaseModel):
    book_name: str
    issue_count: int


# Model for representing a popular book with ID
class PopularBook(BaseModel):
    book_unique_id: int
    book_name: str
    issue_count: int