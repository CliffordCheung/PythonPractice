def organize_contacts(contact_list):
    # Your solution here
    
    # 1. Create helper functions for validation
    # - Function to validate email format
    # - Function to clean and validate phone numbers
    for ind_contact_list in contact_list:
        organized_contact = {}
        name = ind_contact_list["name"]
        email = ind_contact_list["email"]
        phone = ind_contact_list["phone"]
        
        email = email.lower()
        
        print(name, email, phone)
    
        def is_valid_email(email):
          # Check if email has exactly one @ symbol
            if email.count('@') != 1:
                return False
            
            # Split email into local and domain parts
            local, domain = email.split('@')
            
            # Check if both parts exist and email has no spaces
            if not local or not domain or ' ' in email:
                return False
                
            return True
        
        if is_valid_email(email):
            print("hi:", email)
            organized_contact = {
                "name": name,
                "email": email,
                "phone": phone
            }
        
        print(organized_contact)
        #def get_phone_number(phone):
        
        
    
    # 2. Process each contact
    # - Clean email (lowercase) and phone (digits only)
    # - Check if email and phone are valid
    # - Check for duplicates
    
    # 3. Return the clean contact list
    return(organized_contact)
    pass


""" def organize_contacts(contact_list):
    def is_valid_email(email):
        return '@' in email and '.' in email and " " not in email
    
    def clean_phone(phone):
        digits = ''.join(filter(str.isdigit, phone))
        return digits if len(digits) == 10 else None
    
    def clean_contact(contact):
        return {
            'name': contact['name'],
            'email': contact['email'].lower(),
            'phone': clean_phone(contact['phone'])
        }

    cleaned_contacts = []
    seen_emails = set()
    seen_phones = set()
    
    for contact in contact_list:
        cleaned = clean_contact(contact)
        if not is_valid_email(cleaned['email']) or cleaned['phone'] is None:
            continue
        if cleaned['email'] in seen_emails or cleaned['phone'] in seen_phones:
            continue
        seen_emails.add(cleaned['email'])
        seen_phones.add(cleaned['phone'])
        cleaned_contacts.append(cleaned)
    
    return cleaned_contacts """






old_contact_list = [{"name": "John Doe", "email": "JOHN@email.com", "phone": "123-456-7890"}, {"name": "Jane Doe", "email": "jane@email.com", "phone": "123.456.7890"}, {"name": "Bob Smith", "email": "invalid.email", "phone": "12345"}]
new_contact_list = organize_contacts(old_contact_list)
print(new_contact_list)