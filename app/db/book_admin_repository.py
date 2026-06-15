import csv
import os
from typing import Dict
from app.models.book import Book

class CSVBookAdminRepository:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.fieldnames = ["book_id", "title", "author", "price", "count", "is_available"]

    def load_from_csv(self) -> Dict[str, Book]:
        """Reads the CSV and returns a dictionary of {book_id: Book_object}."""
        books = {}
        if not os.path.exists(self.filepath):
            return books  # Return empty dict if file doesn't exist yet

        with open(self.filepath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert string from CSV back to integer
                row['price'] = float(row['price'])
                row['count'] = int(row['count'])
                row['is_available'] = bool(row['is_available'])
                book = Book(**row)
                books[book.book_id] = book
        return books

    def save_to_csv(self, books_dict: Dict[str, Book]):
        """Writes the entire dictionary of books back to the CSV."""
        with open(self.filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            for book in books_dict.values():
                writer.writerow(book.__dict__)