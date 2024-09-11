# School-Library-Management-System
This project implements a simple backend for a school library management system using FastAPI and SQLAlchemy.. Which has the following features:

1.	New Books can be added.
2.	New Students can be registered.
3.	Books inventory can be updated.
4.	Students can issue books and return them.
5.	Display 5 popular books among students along with the number of times they were issued.


# Structure of the application

# Information about the tables and their fields
School library management system has 5 Tables:
1.	Books Table.
2.	Students Table.
3.	Inventory Table.
4.	Transaction Issue Table.
5.	Transaction Return Table.
## Books Table:


Books Table has 4 fields:
1.	book_id: to keep track of a particular row of the "Book Table" data.
2.	book_unique_id: A unique id to keep track of a particular book.
3.	Ibook_name: to store book name.
4.	book_author: to store book author name.

## Students Table:

    
Students Table has 5 fields:
1.	student_id: to keep track of a particular row of the "Students Table" data.
2.	student_id_card_number: A unique id to keep track of a particular Student.
3.	student_name: to store student name.
4.	student_email: to store student email address.
5.	no_of_books_holding: to keep track of no of books a student holding. Note: Here A Student can hold 3 books at a time.

## Inventory Table:


Inventory Table has 3 fields:
1.	inventory_id: to keep track of a particular row of the "Inventory Table" data.
2.	book_unique_id: A unique id to keep track of a particular book, which is stored in the "Book Table". We can store the book_unique_id in the "Inventory Table", only if it is registered or already present in the "Book Table".
3.	no_of_book_copies: to keep track of number of book copies of a particular book.

## Transaction_issue Table:


Transaction_issue Table has 4 fields:
1.	transaction_issue_id: to keep track of a particular row of the "Transaction_issue Table" data.
2.	student_id_card_number: A unique id to keep track of a particular Student, which is stored in the "Students Table".
3.	book_unique_id: A unique id to keep track of a particular book, which is stored in the "Book Table". 
4.	issue_date: to store the data of when the book was distributed.

## Transaction_return Table:


Transaction_return Table has 4 fields:
1.	transaction_return_id: to keep track of a particular row of the "Transaction_return Table" data.
2.	student_id_card_number: A unique id to keep track of a particular Student, which is stored in the "Students Table".
3.	book_unique_id: A unique id to keep track of a particular book, which is stored in the "Book Table". 
4.	return_date: to store the data of when the book was returned.

##  How to start the server:
1.	Clone the repository.
2.	Create Virtual Environment: python -m venv myenv
3.	Install Poetry: pip install poetry  .
4.	Install sqlalchemy: pip install sqlalchemy  .
5.	Install fastapi: pip install "fastapi[standard]".
6.	Install uvicorn: pip install 'uvicorn[standard]'.
7.	Run the Application: uvicorn main:app --reload.
8.	Access the API: The API will be running on http://localhost:8000. Access the interactive API documentation at http://localhost:8000/docs.



   
