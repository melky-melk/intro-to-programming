from book import Book

class Bookshelf:
    def __init__(self, shelf_id):
        self.shelf_id = shelf_id
        self.books = []

    def add_book(self, book):
        """
        Adds a Book object to the bookshelf.

        The book should be added to the end of the all_books list.

        If the parameter is not a Book object, do not add it to the list.
        """
        # type()
        if isinstance(book, Book):
            self.books.append(book)
    
    def remove_book(self, book_title):
        """
        Removes a book from the bookshelf matching the given book title.

        - If the book is found, return the book object
            - If multiple books are found, return the first book found
        - If the book is not found, return None
        """
        i = 0
        while i < len(self.books):
            if self.books[i].title == book_title:
                return self.books.pop(i)
            i += 1
        return None

    def count_books(self):
        """
        Counts the total number of books in the bookshelf.

        Returns the count as an integer.
        """
        return len(self.books)

if __name__ == "__main__":
    # add your own tests
    pass
