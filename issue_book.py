from utils import books, issue_books, data

def issue():
    book_name = input("Enter book name: ").upper()
    if book_name in books:
        print(f'{book_name} is available you have issue it.')
        
        # using roll number of uniqueness and matching
        roll_no = int(input('Enter your Roll Number: '))
        
        # added data of the student and the book in the data dictionary
        if roll_no in data:
            data[roll_no].append(book_name)
        else:
            data[roll_no] = [roll_no, book_name]
    
        # removed one book_name from the books list
        books.remove(book_name)
        # added the book name in the issued_book list
        issue_books.append(book_name)
        
        print("Book assigned successfully")
        
    else:
        print("Book not available")