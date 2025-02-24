contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")
    print()

def search_contact():
    query = input("Enter name or phone number to search: ")
    found = [c for c in contacts if query in c['name'] or query in c['phone']]
    if found:
        for contact in found:
            print(contact)
    else:
        print("No contact found.\n")

def update_contact():
    query = input("Enter name of contact to update: ")
    for contact in contacts:
        if contact['name'] == query:
            contact['phone'] = input("Enter new phone number: ") or contact['phone']
            contact['email'] = input("Enter new email: ") or contact['email']
            contact['address'] = input("Enter new address: ") or contact['address']
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")

def delete_contact():
    query = input("Enter name of contact to delete: ")
    global contacts
    contacts = [c for c in contacts if c['name'] != query]
    print("Contact deleted successfully!\n")

def main():
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.\n")

if __name__ == "__main__":
    main()
