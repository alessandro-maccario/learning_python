from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from main import Book

#################
# get current file path for project folder and define location for saving the db
file_path = os.path.abspath(os.getcwd()) + "/day_63/src/instance/"


# Define the database URL
DATABASE_URL = f"sqlite:///{file_path}new-books-collection.db"

# Create a new SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Define a base class for declarative models
Base = declarative_base()


# Create a session
Session = sessionmaker(bind=engine)
session = Session()


# Function to get a book by ID
def get_book_by_id(book_id):
    return session.query(Book).filter(Book.id == book_id).first()


# Example usage
if __name__ == "__main__":
    # Example: Fetch a book with ID 1
    book = get_book_by_id(1)
    if book:
        print(f"Title: {book.title}, Author: {book.author}")
    else:
        print("Book not found.")
