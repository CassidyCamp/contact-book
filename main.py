from app.contact_book import ContactBook


def main() -> None:

    book = ContactBook()
    
    while True:
        print(
            "1. Add new contact\n"
            "2. Show all contacts\n"
            "3. Search contact by name\n"
            "4. Update contact\n"
            "5. delete contact\n"
            "0. Exit\n"
        )

        choice = input("> ")
        if choice == '1':
            name = input("name: ")
            phone = input("phone: ")
            email = input("email: ")
            book.add_contact(name, phone, email)
        elif choice == '2':
            book.show_all()
        elif choice == '3':
            get_name = input("Enter Searching Name: ")
            book.search_contact(get_name)
        elif choice == '4':
            book.show_all()
            get_task = int(input("Enter Task Number: "))
            book.update_task(get_task)

main()
