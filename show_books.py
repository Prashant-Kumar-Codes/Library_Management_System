from utils import books

# function to show list of books available
def show():
    if not books:
        print("\nCurrently, no books are available in the library.")
    else:
        print("\n--- Available Books ---")
        for i, book_name in enumerate(books, 1):
            print(f"{i}. {book_name}")
        print(f"-----------------------")

# function fot get total number of books 
def get_total_books():
    print(f"\nTotal number of books available in the library: {len(books)}")

def get_books_by_title():
    book_title = input("Enter the name of the book to check its availability: ").upper()
    count = books.count(book_title)
    if count > 0:
        print(f"There are {count} copies of '{book_title}' available.")
    else:
        print(f"'{book_title}' is not currently available in the library.")