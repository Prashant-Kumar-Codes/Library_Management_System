from utils import issue_books, books, data

def return_book():
    roll_no = int(input('Enter your Roll Number: '))
    # condition to check whether it is genuine return or not
    if roll_no not in data:
        print('You have not issued any books')
    else:
        book_name = input("Enter book name: ").upper()
    
        #if book_name in data[roll_no]:
        if data[roll_no][book_name]:
            #data[roll_no].remove(book_name)
            print(data[roll_no][book_name])
            del data[roll_no][book_name]
            
            # removed the roll_no form data dictionary if there are no book left to return
            if len(data[roll_no]) == 0:
                del data[roll_no]
                
            issue_books.remove(book_name)
            books.append(book_name)

            print("Book returned")
            
        else:
            print("You have not issued that book.\nTry again")
