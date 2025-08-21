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

def view_contact(contact_book):
    name = input()
    if name in contact_book:
        print(f'Name: {name}')
        print(f'Phone: {contact_book[name]["phone"]}')
        print(f'Email: {contact_book[name]["email"]}')
        print(f'Address: {contact_book[name]["address"]}')
    else:
        print("Contact not found!")
        
def edit_contact(contact_book):
    name = input()
    if name in contact_book:
        phone_input2 = input()
        email_input2 = input()
        add_input2 = input()
        contact_book[name]={
            "phone": phone_input2,
            "email": email_input2,
            "address": add_input2
        }
        print("Contact updated successfully!")     
    else:
        print("Contact not found!")
        
def delete_contact(contact_book):
    name = input()
    if name in contact_book:
        contact_book[name].pop()
        print("Contact deleted successfully")
    else:
        print("Contact not found!")