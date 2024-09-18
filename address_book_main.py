# UC1 - Create a Contact Class

class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.phone_number}, {self.email}"

#UC2 - add a contact

def add_contact():
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    address = input("Enter Address: ")
    city = input("Enter City: ")
    state = input("Enter State: ")
    zip_code = input("Enter Zip Code: ")
    phone_number = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
    return contact

# Test adding a contact
contact = add_contact()
print(contact)

#UC3 

# address_book_main.py (continuation)

def edit_contact(contact):
    print("Edit Contact Details:")
    contact.first_name = input(f"Edit First Name ({contact.first_name}): ") or contact.first_name
    contact.last_name = input(f"Edit Last Name ({contact.last_name}): ") or contact.last_name
    contact.address = input(f"Edit Address ({contact.address}): ") or contact.address
    contact.city = input(f"Edit City ({contact.city}): ") or contact.city
    contact.state = input(f"Edit State ({contact.state}): ") or contact.state
    contact.zip_code = input(f"Edit Zip Code ({contact.zip_code}): ") or contact.zip_code
    contact.phone_number = input(f"Edit Phone Number ({contact.phone_number}): ") or contact.phone_number
    contact.email = input(f"Edit Email ({contact.email}): ") or contact.email
    return contact

# Example usage
contact = add_contact()
print(contact)
edited_contact = edit_contact(contact)
print(edited_contact)
