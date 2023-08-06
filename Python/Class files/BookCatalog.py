import json

'''Build a book catalog application that enables users to keep track of their book collection. #
Users can add books with details such as title, author, genre, 
and publication year. The program will store the book data in a 
file or a database and provide functionalities to view, search, 
and update book information.'''

class BookCatalog:
    def __init__(self, filename):
        self.filename = filename
        self.books = []

    def add_book(self, title, author, genre, publication_year):
        book = {"title": title, "author": author, "genre": genre, "publication_year": publication_year}
        self.books.append(book)
        self.save_to_file()

    def save_to_file(self):
        with open(self.filename, "w") as file:
            json.dump(self.books, file)

    def load_from_file(self):
        try:
            with open(self.filename, "r") as file:
                self.books = json.load(file)
        except FileNotFoundError:
            pass

    def view_books(self):
        for book in self.books:
            print(f"Title: {book['title']}\nAuthor: {book['author']}\nGenre: {book['genre']}\nPublication Year: {book['publication_year']}\n")

# Usage example
catalog = BookCatalog("books.json")
catalog.add_book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1925)
catalog.add_book("To Kill a Mockingbird", "Harper Lee", "Fiction", 1960)
catalog.load_from_file()
catalog.view_books()
