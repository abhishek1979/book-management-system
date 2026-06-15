from fastapi import APIRouter
from app.services.book_admin_service import BookAdminService
from app.schemas.book import Book
from app.core.logger import logger

class BookAdminAPI:

    def __init__(self):
        self.router = APIRouter()
        self.book_admin_service = BookAdminService()
        
        # Route registration
        self.router.add_api_route(
            "/add_book", 
            self.add_book, 
            methods=["POST"], 
            summary="Add new Book to Data Disctionary.", 
            description="This API will add Book to Data Dictionary and if that book already exists, then it returns Book Aleardy Exists message otherwise Book Detail", 
            response_description="Returns newly added Book Detail in JSON Format")
        
        self.router.add_api_route("/update_book", 
            self.update_book, 
            methods=["PUT"], 
            summary="Update existing Book to Data Disctionary.", 
            description="This API will update Book to Data Dictionary and if that book does not exists, then it returns Book does not Exists message otherwise Book Detail", 
            response_description="Returns newly updated Book Detail in JSON Format")
        
        self.router.add_api_route("/delete_book/{book_id}", 
            self.delete_book, 
            methods=["DELETE"], 
            summary="Deletes Book from Data Disctionary.", 
            description="This API will delete Book from Data Dictionary and if that book does not exists, then it returns Book does not Exists message otherwise deleted Book ID",
            response_description="Returns newly updated Book Detail in JSON Format")
        
        self.router.add_api_route("/get_book", self.get_book, methods=["GET"])
        self.router.add_api_route("/get_all_books", self.get_all_books, methods=["GET"])   
    
    def add_book(self, book: Book):
        logger.info("Book has been added successfully.")
        return self.book_admin_service.add_book(book)
    
    def update_book(self, book: Book):
        logger.info("Book has been updated successfully.")
        return self.book_admin_service.update_book(book)
    
    def delete_book(self, book_id: str):
        logger.info("Book has been deleted successfully.")
        return self.book_admin_service.delete_book(book_id)
    
    def get_book(self, book_id: str):
        logger.info("Book has been fetched successfully.")
        return self.book_admin_service.get_book(book_id)
    
    def get_all_books(self):
        logger.info("All books have been fetched successfully.")
        return self.book_admin_service.get_all_books()

