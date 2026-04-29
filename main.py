

from datetime import datetime, timedelta



books = {
    1: {"title": "Things Fall Apart", "available": True},
    2: {"title": "Half of a Yellow Sun", "available": True},
    3: {"title": "Intro to Algorithms", "available": True}
}

borrowed = {}



def get_books():
    print("\n Available Books:")
    for book_id, book in books.items():
        status = "Available" if book["available"] else "Borrowed"
        print(f"{book_id}. {book['title']} - {status}")



def borrow_book():
    user_id = input("Enter User ID: ")
    book_id = int(input("Enter Book ID: "))

    if book_id not in books:
        print("Book not found")
        return

    if not books[book_id]["available"]:
        print(" Book not available")
        return

    due_date = datetime.now() + timedelta(days=7)

    books[book_id]["available"] = False
    borrowed[book_id] = {
        "user_id": user_id,
        "due_date": due_date
    }

    print(f"Book borrowed! Due date: {due_date.date()}")



def return_book():
    user_id = input("Enter User ID: ")
    book_id = int(input("Enter Book ID: "))

    if book_id not in borrowed:
        print(" Book was not borrowed")
        return

    record = borrowed[book_id]

    if record["user_id"] != user_id:
        print(" Unauthorized return")
        return

    today = datetime.now()
    due_date = record["due_date"]

    days_late = (today - due_date).days
    fine = max(0, days_late * 2)

    books[book_id]["available"] = True
    borrowed.pop(book_id)

    print(f" Book returned! Fine: {fine}")



def check_overdue():
    user_id = input("Enter User ID: ")

    print("\n Overdue Books:")
    found = False

    for book_id, record in borrowed.items():
        if record["user_id"] == user_id:
            days_late = (datetime.now() - record["due_date"]).days

            if days_late > 0:
                fine = days_late * 2
                print(f"Book ID {book_id} | Days overdue: {days_late} | Fine: {fine}")
                found = True

    if not found:
        print(" No overdue books")



def menu():
    while True:
        print("\n===== LIBRARY MENU =====")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Check Overdue")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            get_books()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            check_overdue()
        elif choice == "5":
            print(" Goodbye!")
            break
        else:
            print(" Invalid option")



menu()