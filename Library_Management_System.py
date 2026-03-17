
'''
The Library Management System is a Terminal based project made using the Object Oriented Progamming and Python  
which basically helps in the overall management of the library. This is a mini level terminal based project. 

The main features of the Library Management System include the: 
 1. Adding of a new book 
 2. Dsiplay all the books 
 3. Issue a book 
 4. Return a book 
 5. Search a book 

''' 
class Library: 
    def __init__(self): 
        self.books = [] 

    def add_book(self, book): 
        self.books.append(book) 
        print("Books added successfully") 

    def display_books(self): 
        if not self.books: 
            print("No books available") 
        else: 
            print("\nAvailable Books:")
            for book in self.books: 
                print(book) 

    def issue_book(self, book): 
        if book in self.books: 
            self.books.remove(book)
            print("Book issued successfully") 
        
        else: 
            print("Book not available") 

    def return_book(self, book): 
        self.books.append(book)
        print("Book returned successfully") 

    def search_book(self, book): 
        if book in self.books: 
            print("Book is available in library") 

        else: 
            print("Book not found")  

library = Library()  

while True: 
    print("\n======Library Management System======") 
    print("1. Add Book") 
    print("2. Display Books") 
    print("3. Issue Book")
    print("4. Return Book") 
    print("5. Search Book") 
    print("6. Exit") 

    choice = int(input("Enter your choice: ")) 

    if choice == 1: 
        book = input("Enter the book name: ") 
        library.add_book(book)

    elif choice == 2: 
        library.display_books() 

    elif choice == 3: 
        book = input("Enter the book name to issue: ")
        library.issue_book(book) 

    elif choice == 4: 
        book =  input("Enter the book name to return: ")
        library.return_book(book) 

    elif choice == 5: 
        book = input("Enter the book name to search: ")
        library.search_book(book) 

    elif choice == 6: 
        print("Exiting program.......")
        break 

    else: 
        print("Invalid Choice")  



