from utils import issue_books, books, data
from datetime import datetime

def return_book():
    roll_no = int(input('Enter your Roll Number: '))
    # condition to check whether it is genuine return or not
    if roll_no not in data:
        print('You have not issued any books')
    else:
        book_name = input("Enter book name: ").upper()
    
        #if book_name in data[roll_no]:
        if book_name in data[roll_no]:
            issue_date = data[roll_no][book_name]
            print(f"Book issued on: {issue_date}")
            
            # logic for fine implementation
            '''
            - Give a proper notice that after certain period of date charges will be applied like:
            for 1 week - 10Rs/day/book
            2nd week - 10*2/day/book
            3rd week - 10*2*3/day/book
            Like that continue
            '''
            
            # Calculate days overdue
            days_overdue = (datetime.now() - issue_date).days
            
            # Calculate fine based on weeks overdue
            fine = 0
            if days_overdue > 10:
                weeks = (days_overdue - 10) // 7
                for week_num in range(1, weeks + 1):
                    fine += 10 * week_num  # 10Rs/day for week 1, 20Rs/day for week 2, etc.
                
                # Add fine for remaining days
                remaining_days = (days_overdue - 10) % 7
                fine += 10 * (weeks + 1) * remaining_days
                
                print(f"You have overdue by {days_overdue} days. Fine: {fine} Rs")
            
            del data[roll_no][book_name]
            
            # removed the roll_no form data dictionary if there are no book left to return
            if len(data[roll_no]) == 0:
                del data[roll_no]
                
            issue_books.remove(book_name)
            books.append(book_name)

            print("Book returned successfully")
            
        else:
            print("You have not issued that book.\nTry again")
