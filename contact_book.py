# Define a dictionary to store contacts (name as key and contact details as value)
contacts = {}

def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")
    
    contact = {
        'Phone': phone,
        'Email': email,
        'Address': address
    }

    contacts[name] = contact
    print(f"Contact '{name}' added successfully!")

def view_contact_list():
    if not contacts:
        print("Contact list is empty.")
    else:
        print("Contact List:")
        for name in contacts:
            print(f"Name: {name}")
            print(f"Phone: {contacts[name]['Phone']}")
            print(f"Email: {contacts[name]['Email']}")
            print(f"Address: {contacts[name]['Address']}")
            print("-" * 20)

def search_contact():
    search_term = input("Enter a name or phone number to search: ").lower()
    found = False

    for name in contacts:
        if search_term in name.lower() or search_term in contacts[name]['Phone']:
            print(f"Name: {name}")
            print(f"Phone: {contacts[name]['Phone']}")
            print(f"Email: {contacts[name]['Email']}")
            print(f"Address: {contacts[name]['Address']}")
            found = True

    if not found:
        print("No matching contacts found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("Enter new details (leave blank to keep existing):")
        phone = input(f"Phone ({contacts[name]['Phone']}): ")
        email = input(f"Email ({contacts[name]['Email']}): ")
        address = input(f"Address ({contacts[name]['Address']}): ")

        if phone:
            contacts[name]['Phone'] = phone
        if email:
            contacts[name]['Email'] = email
        if address:
            contacts[name]['Address'] = address

        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"'{name}' not found in contacts.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"'{name}' not found in contacts.")

def main():
    print("Welcome to the Contact Book!")
    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact_list()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Thank you for using the Contact Book!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
