from app.schemas.book import Book
from app.core.logger import logger
import json

class BookAdminService:

    def __init__(self):
        print("Book Instance has been created.")
    
    def add_book(self, book: Book):
        logger.info(f"Book for Save : {book.model_dump_json(indent=4)}" )
        return "Book has been added successfully."

    def update_book(self, book: Book, book_id: int):
        logger.info(f"Book for Update : {book.model_dump_json(indent=4)}" )
        return f"Book {book_id} has been updated successfully."    
    
    def delete_book(self, book_id: int):
        logger.info(f"Book Id : {book_id} for deletion.")
        return f"Book {book_id} has been deleted successfully."    
        
    def get_book(self, book_id: int):
        logger.info(f"Book Id : {book_id} for fetch.")
        return f"Book {book_id} has been fetched successfully."
    
    def get_all_books(self):        
        logger.info("All books have been fetched successfully.")
        return "All books havr been fetched successfully."