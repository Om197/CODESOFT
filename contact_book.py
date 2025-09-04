
def contact_book():
    contacts = []
    while True:
        print("1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
            print("Contact added.")
        elif choice == '2':
            for i, c in enumerate(contacts):
                print(f"{i+1}. {c['name']} - {c['phone']}")
        elif choice == '3':
            search = input("Search by name or phone: ").lower()
            found = [c for c in contacts if search in c['name'].lower() or search in c['phone']]
            for c in found:
                print(c)
        elif choice == '4':
            idx = int(input("Contact number to update: ")) - 1
            if 0 <= idx < len(contacts):
                print("Updating contact...")
                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email: ")
                address = input("Address: ")
                contacts[idx] = {'name': name, 'phone': phone, 'email': email, 'address': address}
                print("Contact updated.")
        elif choice == '5':
            idx = int(input("Contact number to delete: ")) - 1
            if 0 <= idx < len(contacts):
                contacts.pop(idx)
                print("Contact deleted.")
        elif choice == '6':
            break
        else:
            print("Invalid choice.")
    print("Exiting Contact Book.")

contact_book()
