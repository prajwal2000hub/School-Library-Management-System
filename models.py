from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define the Book model
class Book(Base):
    __tablename__ = "books"

# Define the columns for the Book table
    book_id = Column(Integer, primary_key=True, index=True)
    book_unique_id = Column(String, unique=True, nullable=False)
    book_name = Column(String, nullable=False)
    book_author = Column(String, nullable=False)
    inventory = relationship("Inventory", backref="book", uselist=False, cascade="all, delete-orphan")


# Define the Student model
class Student(Base):
    __tablename__ = "students"

# Define the columns for the Student table
    student_id = Column(Integer, primary_key=True, index=True)
    student_id_card_number = Column(String, unique=True, nullable=False)
    student_name = Column(String, nullable=False)
    student_email = Column(String, unique=True, nullable=False)
    no_of_books_holding = Column(Integer, CheckConstraint("no_of_books_holding <= 3"), default=0)
    transactions = relationship("TransactionIssue", backref="student")


# Define the Inventory model
class Inventory(Base):
    __tablename__ = "inventory"

# Define the columns for the Inventory table
    inventory_id = Column(Integer, primary_key=True, index=True)
    book_unique_id = Column(String, ForeignKey("books.book_unique_id"), nullable=False)
    no_of_book_copies = Column(Integer, default=0)


# Define the TransactionIssue model
class TransactionIssue(Base):
    __tablename__ = "transaction_issue"

# Define the columns for the TransactionIssue table
    transaction_issue_id = Column(Integer, primary_key=True, index=True)
    student_id_card_number = Column(String, ForeignKey("students.student_id_card_number"), nullable=False)
    book_unique_id = Column(String, ForeignKey("books.book_unique_id"), nullable=False)
    issue_date = Column(String, nullable=False)


# Define the TransactionReturn model
class TransactionReturn(Base):
    __tablename__ = "transaction_return"

# Define the columns for the TransactionReturn table
    transaction_return_id = Column(Integer, primary_key=True, index=True)
    student_id_card_number = Column(String, ForeignKey("students.student_id_card_number"), nullable=False)
    book_unique_id = Column(String, ForeignKey("books.book_unique_id"), nullable=False)
    return_date = Column(String, nullable=False)