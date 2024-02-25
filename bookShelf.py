class Book: 

    def __init__(self,title, author, year):
        self.title = title
        self.author = author
        self.year = year


class BookManager:

    def __init__(self):
        self.books = []

    def add_book(self, book : Book):
        self.books.append(book)
        print(f"Book '{book.title}' added to shelf")


    def show_all_books(self):
        if self.books:
            print("Listing all books:")
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}\n")
        else:
            print("No books on shelf")

    def find_book_with_title(self, title: str):
        found_books = []  
        for book in self.books:
            if book.title == title:
                found_books.append(book)  

        if len(found_books) != 0:
            print(f"Found {len(found_books)} book(s) with title '{title}':")
            for book in found_books:
                print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}")
        else:
            print(f"There is not book with title :{title}")

if __name__ == "__main__":
    manager = BookManager()
    while True:

        operation = input("choose what you want to do:\n type 'a' to add new book\n type 's' to show all books\n type 'f' to find book with it's title\n type 'q' to quit program\n")
        
        if operation == 'a':
    
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter book year: ")
            try:
                year = int(year)
            except ValueError:
                print("Please enter valid year")
                continue
            if year < 0 or year > 2024:  
                print("Please enter valid year")
                continue

                
            
            book = Book(title, author, year)
            manager.add_book(book)
        
        if operation == 's':
            manager.show_all_books()
        
        if operation == 'f':
            manager.find_book_with_title("1984")

        if operation == 'q':
            break