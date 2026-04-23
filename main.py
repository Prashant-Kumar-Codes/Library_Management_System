from add_books import add
from issue_book import issue
from show_books import show, get_total_books, get_books_by_title
from return_book import return_book
from utils import data

def library():
    while True:
        print("\n1. Add Book\n2. Show Book\n3. Issue Book\n4. Return Book\n5. Show Total Number of Books\n6. Search Book by Title\n7. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        try:
            if choice=='1':
                add()
            elif choice=='2':
                show()
                
            elif choice=='3':
                issue()
                
            elif choice=='4':
                return_book()
                
            elif choice=='5':
                get_total_books()
                
            elif choice=='6':
                get_books_by_title()
                
            elif choice=='7': 
                print("Thank you")
                break
            
            elif choice == 'data':
                print(data)
            else:
                print("Invalid choice")
        
        except Exception as e:
            print('Invalid input')
            print(f'Got error: {e}')
            print('Use valid inputs\n')
library()