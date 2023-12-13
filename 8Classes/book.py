class Book:
    def __init__(self, title, num_pages, price):
        
        self.title = title
        self.num_pages = num_pages
        self.price = price

    def update_price(self, price):
        """
        Changes the price of the book to the new price provided.
        """
        self.price = price

    def calculate_price_per_page(self):
        """
        Calculates the price per page (price / page).

        Returns the result rounded to 2 decimal places.
        """
        return round((self.price / self.num_pages), 2)

    def get_most_economical(books):
        """
        From a list of Book objects, returns the book with the lowest price per page.
        """
        
        # we want to loop through the books and find the lowest oct
        # we need to keep track of which is the lowest book 

        # set this to ridculous high value so it will be replaced later in the if statement
        lowest_price_per_page = 99999999999999
        cheapest_book = None #initialise a cheapest_book

        i = 0 
        while i < len(books):
            curr_book = books[i]
            
            # when we find a value that is smaller than our smallest price per page
            if curr_book.calculate_price_per_page() < lowest_price_per_page:
                # we replace the lowest price with, the new lowest price and set our cheapest book
                lowest_price_per_page = curr_book.calculate_price_per_page()
                cheapest_book = curr_book

            i += 1

        return cheapest_book

        # 90, 20, 30, 10

if __name__ == "__main__":

    # Some sample code
    book_1 = Book("Stranger in a Strange Land", 408, 16.32)
    print(book_1.title)
    book_2 = Book("Rendezvous with Rama", 256, 13.99)
    book_3 = Book("Twilight", 498, 12.00)
    book_4 = Book("I Want to Eat Your Pancreas", 260, 26.36)

    assert book_1.calculate_price_per_page() == 0.04

    book_list = [book_1, book_2, book_3, book_4]
    best_book = Book.get_most_economical(book_list)
    print("The most economical book is {}".format(best_book.title))

    # What's the difference between the following lines? Which one is the best?

    book_1.update_price(19.99)
    Book.update_price(book_1, 19.99)
    book_1.price = 19.99
