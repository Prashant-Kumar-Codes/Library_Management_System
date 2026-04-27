from utils import issue_books, books, data
from datetime import datetime
import math

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
            
            Pattern: Week N → 10 * N! Rs/day
            '''
            
            # Calculate days overdue
            days_overdue = (datetime.now() - issue_date).days
            
            # Calculate fine based on weeks overdue
            fine = 0
            if days_overdue > 10:
                overdue_days = days_overdue - 10
                
                # Full weeks
                weeks = overdue_days // 7
                for week_num in range(1, weeks + 1):
                    daily_rate = 10 * math.factorial(week_num)  # 10 * N!
                    fine += daily_rate * 7
                
                # Remaining days in the current week
                remaining_days = overdue_days % 7
                if remaining_days > 0:
                    daily_rate = 10 * math.factorial(weeks + 1)
                    fine += daily_rate * remaining_days
                
                print(f"You have overdue by {days_overdue} days. Fine: {fine} Rs")
                
            else:
                print('You have no overdues to pay')
                
            # removed the book data of that roll no
            del data[roll_no][book_name]

            # removed the roll_no form data dictionary if there are no book left to return
            if len(data[roll_no]) == 0:
                del data[roll_no]
                
            issue_books.remove(book_name)
            books.append(book_name)

            print("Book returned successfully")
            
        else:
            print("You have not issued that book.\nTry again")
            
