"""Contact Book Application"""

# Initialize an empty contact book 
contacts = {}

while True:
    # Display menu 
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    # Get user choice 
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        # Add contact 
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        contacts[name] = {"phone":phone, "email": email}
        print("Contact added!")

    elif choice == "2":
        # View contact 
        if not contacts:
            print("No contacts in the contact book.")
        else:
            print("\nContacts:")
            for name, info in contacts.items():
                print(f"Name: {name}")
                print(f"Phone: {info['phone']}")
                print(f"Email: {info['email']}")
                print("-" * 20)

    elif choice == "3":
        # Search contact 
        name = input("Enter name to search: ")
        if name in contacts:
            info = contacts[name]
            print(f"\nName: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
        else:
            print("Contact not found.") 

    elif choice == "4":
        # Delete contact 
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted!")
        else:
            print("Contact not found.")

    elif choice == "5":
        # Exit 
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again...")