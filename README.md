# School-Library-Management-System
This project implements a simple backend for a school library management system using FastAPI and SQLAlchemy.. Which has the following features:

1.	New Books can be added.
2.	New Students can be registered.
3.	Books inventory can be updated.
4.	Students can issue books and return them.
5.	Display 5 popular books among students along with the number of times they were issued.
![image](https://github.com/user-attachments/assets/48c358ec-07eb-421a-9e29-0c823be1ad88)


# Structure of the application
![image](https://github.com/user-attachments/assets/5f625bdf-1678-4c8d-93f4-532c2e48410b)

# Information about the tables and their fields
School library management system has 5 Tables:
1.	Books Table.
2.	Students Table.
3.	Inventory Table.
4.	Transaction Issue Table.
5.	Transaction Return Table.
## Books Table:
![image](https://github.com/user-attachments/assets/21c9814c-a8ef-4bcd-8b1b-14e28a4a0c12)

Books Table has 4 fields:
1.	book_id: to keep track of a particular row of the "Book Table" data.
2.	book_unique_id: A unique id to keep track of a particular book.
3.	Ibook_name: to store book name.
4.	book_author: to store book author name.

## Students Table:
![image](https://github.com/user-attachments/assets/da1dbbb9-f48a-4f32-8cff-80c3e849d919)
    
Students Table has 5 fields:
1.	student_id: to keep track of a particular row of the "Students Table" data.
2.	student_id_card_number: A unique id to keep track of a particular Student.
3.	student_name: to store student name.
4.	student_email: to store student email address.
5.	no_of_books_holding: to keep track of no of books a student holding. Note: Here A Student can hold 3 books at a time.

## Inventory Table:
![image](https://github.com/user-attachments/assets/4ad6c37b-5e17-4290-8959-70cf6edaaf3c)

Inventory Table has 3 fields:
1.	inventory_id: to keep track of a particular row of the "Inventory Table" data.
2.	book_unique_id: A unique id to keep track of a particular book, which is stored in the "Book Table". We can store the book_unique_id in the "Inventory Table", only if it is registered or already present in the "Book Table".
3.	no_of_book_copies: to keep track of number of book copies of a particular book.

## Transaction_issue Table:
![image](https://github.com/user-attachments/assets/aa147910-ddd8-4890-85b0-cbe1e05e57fa)

Transaction_issue Table has 4 fields:
1.	transaction_issue_id: to keep track of a particular row of the "Transaction_issue Table" data.
2.	student_id_card_number: A unique id to keep track of a particular Student, which is stored in the "Students Table".
3.	book_unique_id: A unique id to keep track of a particular book, which is stored in the "Book Table". 
4.	issue_date: to store the data of when the book was distributed.

## Transaction_return Table:
![image](https://github.com/user-attachments/assets/570ef37d-d7e0-4a65-88eb-19ef805361fb)

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

##  Working of the School Library Management System:
### Add A Book:
![image](https://github.com/user-attachments/assets/9452b5b3-0ccb-43d2-908c-c739df93d804)
### Updating Books Table
![image](https://github.com/user-attachments/assets/ae89557e-b5e7-45b7-abe9-6360e7bbcf3e)

### Add New Student: 
![image](https://github.com/user-attachments/assets/c2964130-b264-4f1b-96a1-72b56941991d)

### Updating Students Table:
![image](https://github.com/user-attachments/assets/079c5b99-fe4f-435c-8ee2-714f06dbc246)

### Add Inventory:
![image](https://github.com/user-attachments/assets/cb6f0eaa-b82e-4606-a4a8-9e6c633817d8)

### Updating Inventory Table:
![image](https://github.com/user-attachments/assets/78a07284-5776-4bbd-ba62-d97e6e000e1e)

### Throws Error If Book ID not found in Books Table:
![image](https://github.com/user-attachments/assets/d26d5cac-0797-4997-a4d7-250483799f90)

### Update Inventory:
![image](https://github.com/user-attachments/assets/6d0d09d8-0242-41c7-a97b-01f2514fb2f7)

### Updating Inventory Table:
![image](https://github.com/user-attachments/assets/908cf563-4f74-46c8-9126-8bdf24444daf)

### Issue Book:
![image](https://github.com/user-attachments/assets/71ff136c-6eab-4780-9219-d37c64d26c29)

### Updating Transaction_Issue Table:
![image](https://github.com/user-attachments/assets/13ed8a76-6019-4d78-9566-24fd14eda710)

### Updating Students Table:
![image](https://github.com/user-attachments/assets/3e422f87-70a5-4ca5-9c52-a61b3617dc5b)

### Updating Inventory Table:
![image](https://github.com/user-attachments/assets/07866439-0fcf-4387-aa77-80288bb54403)

### Throws Error if we request the Book, That is not Available:
![image](https://github.com/user-attachments/assets/4bd1a3ed-d6ae-43f6-a75b-e4851b22efe8)

### Return Book:
![image](https://github.com/user-attachments/assets/fa3a86f0-5a31-4431-abe2-e9149dd095ee)

### Updating Transaction_Return Table:
![image](https://github.com/user-attachments/assets/820dba08-284d-4756-80d4-20ce18f79a7f)

### Updating Students Table:
![image](https://github.com/user-attachments/assets/8d1bd69b-4126-4b89-8ff7-96929b445c90)

### Updating Inventory Table:
![image](https://github.com/user-attachments/assets/adfcad4f-fc7c-4ae9-afc7-478bc90edbca)

### Get 5 Popular Books:
![image](https://github.com/user-attachments/assets/af24c59e-7ff7-43ab-824c-28d0998da85a)



   
