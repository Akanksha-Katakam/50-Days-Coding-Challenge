# Day 2 -> Simple Library Management System

books = []

# To add a new book
def add_book():
    book = input("Enter a Book Name: ")
    books.append(book)
    print(f"{book} has been added successfully!")
    
# To display all books
def view_books():
    if len(books) == 0:
        print("No books available in the library")
    else:
        print(" Library Books ".center(50,"="))
        for i in range(len(books)):
           print(f"{i+1}. {books[i]}")
        print("="*50)
 
# To search a book
def search_book():
    book = input("Enter book name to search: ")
    if book in books:
        print(f"{book} is available in the library")
    else:
        print(f"{book} is not available")

# To remove a book
def remove_book():
    book = input("Enter book name to remove: ")
    if book in books:
        books.remove(book)
        print(f"{book} has been removed successfully")
    else:
        print(f"{book} not found")
        
while True:
    print(" Library Management System ".center(50,"="))
    print("1. Add book")
    print("2. View books")
    print("3. Search books")
    print("4. Remove books")
    print("5. Exit")
    print("="*50)

    choice = input("Enter your choice: ")
    match choice:
        # Add book
        case "1":
            add_book()
        # Display all books
        case "2":
            view_books()
        # Search for a book
        case "3":
            search_book()
        # Remove a book
        case "4":
            remove_book()
        case "5":
            print("Thank you !")
            break
        case _:
            print("Invalid choice! please enter a number between 1 and 5")
        
            
            
