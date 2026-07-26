# CONTACT BOOK

contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        contacts[name] = phone
        print("Contact Added Successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No Contacts Found.")
        else:
            print("\nContact List")
            for name, phone in contacts.items():
                print("Name:", name, "| Phone:", phone)

    elif choice == "3":
        name = input("Enter Name to Search: ")
        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact Not Found.")

    elif choice == "4":
        name = input("Enter Name to Delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact Deleted Successfully!")
        else:
            print("Contact Not Found.")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again.")