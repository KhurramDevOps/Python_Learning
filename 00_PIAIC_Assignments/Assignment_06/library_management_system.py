print("Welcome to the Community Library System!")
print("----------------------------------------")

book = [
    {"ID": 1, "title": "1984", "author": "George Orwell", "genre": "Dystopian", "status": "Available"},
    {"ID": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "status": "Available"},
    {"ID": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classics", "status": "Borrowed"}
]
users = [
    {"ID": 1, "name": "John Doe", "borrowed_books": []},
    {"ID": 2, "name": "Jane Smith", "borrowed_books": [3]}
]

def view_books():
    for x in book:
        print(f"{x['ID']} {x['title']} {x['author']} {x['status']}")

def search_book():
    search = input("\nEnter the book title you want to search: ")
    found = False
    for x in book:
        if search.lower() in x["title"].lower():
            print(f"{x['ID']} {x['title']} {x['author']} {x['genre']} {x['status']}")
            found = True
    if not found:
        print("Book not found")

def borrow_book():
    user_id = int(input("\nEnter your User ID : "))
    search = int(input("Enter the book ID you want to borrow: "))
    for x in book:
        if search == x["ID"]:
            if x["status"] == "Available":
                x["status"] = "Borrowed"
                users[1]["borrowed_books"].append(x["ID"])
                print("Book borrowed successfully")
            else:
                print("Book is not available.")
            return
    print("Invalid ID")

def return_book():
    input("\nEnter you User ID : ")
    search = int(input("Enter the book ID you want to return: "))
    for i in book:
        if search == i["ID"]:
            if i["status"] == "Borrowed":
                i["status"] = "Available"
                users[1]["borrowed_books"].remove(i["ID"])
                print("Book returned successfully")
            else:
                print("This book wasn't borrowed.")
            return
    print("Invalid ID")

def view_users():
    for x in users:
        print(f"{x['ID']}  {x['name']} {x['borrowed_books']}")

def exit_system():
    print("\nThank you for using the Community Library System!")
    print("--------------------------------------------------")
    exit()  # Exits the program

while True:
    print("Please choose an option: ")
    print("1. View all books")
    print("2. Search for a book")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. View all users")
    print("6. Exit")

    choice = int(input("\nEnter your choice [1,2,3,4,5,6]: "))

    if  choice == 1:
        view_books()
    elif choice == 2:
        search_book()
    elif choice == 3:
        borrow_book()
    elif choice == 4:
        return_book()
    elif choice == 5:
        view_users()
    elif choice == 6:
        exit_system()
    else:
        print("Invalid choice. Please choose a valid option.")
    print("----------------------------------------")
