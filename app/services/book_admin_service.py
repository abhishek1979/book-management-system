from typing import List, Optional, Dict
from app.schemas.book import Book
from app.core.logger import logger
import json
from app.db.book_admin_repository import CSVBookAdminRepository

class BookAdminService:

    def __init__(self):
        self.repository = CSVBookAdminRepository("book_library.csv")
        # Load the dictionary from the CSV right when the service starts
        self.books_dict: Dict[str, Book] = self.repository.load_from_csv()
        logger.info(f"Inside __init__() : Books Available : {self.books_dict}")
        print("Book Instance has been created.")

    def get_all_books(self) -> List[Book]:
        logger.info(f"Get All Books : {self.books_dict.values()}")
        return list(self.books_dict.values())

    def get_book(self, book_id: str) -> Optional[Book]:
        return self.books_dict.get(book_id)

    def add_book(self, book_request: Book) -> Book:
        logger.info(f"Inside add_book() : : Available Book List : {self.books_dict}")
        if book_request.book_id in self.books_dict:
            raise ValueError(f"Book with ID '{book_request.book_id}' already exists.")
        
        self.books_dict[book_request.book_id] = book_request
        self.repository.save_to_csv(self.books_dict)
        return book_request   
    
    def update_book(self, book_request: Book) -> Book:
        logger.info(f"Inside update_book() : : Available Book List : {self.books_dict}")
        logger.info(book_request.book_id in self.books_dict)
        if book_request.book_id not in self.books_dict:
            raise KeyError(f"Book with ID '{book_request.book_id}' not found.")
        
        book = self.books_dict[book_request.book_id]

        book.title = book_request.title
        book.author = book_request.author
        book.price = book_request.price
        book.count = book_request.count
        book.is_available = book_request.is_available
                
        self.repository.save_to_csv(self.books_dict)
        return book   
    
    def delete_book(self, book_id: str):
        logger.info(f"Inside delete_book() : : Available Book List : {self.books_dict}")
        logger.info(book_id in self.books_dict)
        if book_id not in self.books_dict:
            raise KeyError(f"Book with ID '{book_id}' not found.")
        
        del self.books_dict[book_id]
        self.repository.save_to_csv(self.books_dict)   
