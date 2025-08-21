def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")
    
def add_contact(contact_book):
    name_input = input()
    phone_input = input()
    email_input = input()
    add_input = input()
    if name_input in contact_book:
        print("Contact already exists!")
    else:
        contact_book[name_input] = {
            "phone": phone_input,
            "email": email_input,
            "address": add_input
        }
        print("Contact added successfully!")