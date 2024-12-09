import json
import os
import re

# File to store contacts
CONTACTS_FILE = 'contacts.json'

# Load existing contacts from the file (if any)
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

# Save contacts to the file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Display all contacts
def display_contacts(contacts):
    if len(contacts) == 0:
        print("No contacts found!")
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

# Function to validate phone number (must be 10 digits starting with +91)
def is_valid_phone(phone):
    return bool(re.match(r'^\+91\d{10}$', phone))

# Function to validate email address
def is_valid_email(email):
    return bool(re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email))

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    
    # Phone validation
    while True:
        phone = input("Enter phone number (+91 followed by 10 digits): ")
        if is_valid_phone(phone):
            break
        else:
            print("Invalid phone number. Please enter a valid phone number with +91 and 10 digits.")
    
    # Email validation
    while True:
        email = input("Enter email address: ")
        if is_valid_email(email):
            break
        else:
            print("Invalid email address. Please enter a valid email.")
    
    address = input("Enter address: ")

    new_contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }

    contacts.append(new_contact)
    print(f"Contact '{name}' added successfully!")

# Update an existing contact
def update_contact(contacts):
    display_contacts(contacts)
    try:
        contact_index = int(input("Enter the number of the contact you want to update: ")) - 1
        if contact_index < 0 or contact_index >= len(contacts):
            print("Invalid choice!")
            return

        print("Leave the field empty if you don't want to update it.")
        name = input(f"Enter new name (current: {contacts[contact_index]['name']}): ")
        
        # Phone validation
        while True:
            phone = input(f"Enter new phone number (current: {contacts[contact_index]['phone']}): ")
            if not phone and contacts[contact_index]['phone']:
                phone = contacts[contact_index]['phone']  # Keep existing phone number if input is empty
            if not phone or is_valid_phone(phone):
                break
            else:
                print("Invalid phone number. Please enter a valid phone number with +91 and 10 digits.")
        
        # Email validation
        while True:
            email = input(f"Enter new email (current: {contacts[contact_index]['email']}): ")
            if not email and contacts[contact_index]['email']:
                email = contacts[contact_index]['email']  # Keep existing email if input is empty
            if not email or is_valid_email(email):
                break
            else:
                print("Invalid email address. Please enter a valid email.")
        
        address = input(f"Enter new address (current: {contacts[contact_index]['address']}): ")

        if name:
            contacts[contact_index]['name'] = name
        if phone:
            contacts[contact_index]['phone'] = phone
        if email:
            contacts[contact_index]['email'] = email
        if address:
            contacts[contact_index]['address'] = address

        print("Contact updated successfully!")
    except ValueError:
        print("Please enter a valid number.")

# Delete a contact
def delete_contact(contacts):
    display_contacts(contacts)
    try:
        contact_index = int(input("Enter the number of the contact you want to delete: ")) - 1
        if contact_index < 0 or contact_index >= len(contacts):
            print("Invalid choice!")
            return

        deleted_contact = contacts.pop(contact_index)
        print(f"Contact '{deleted_contact['name']}' deleted successfully!")
    except ValueError:
        print("Please enter a valid number.")

# Search for a contact
def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ").lower()
    results = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone'].lower()]
    
    if results:
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No matching contacts found.")

# Main menu
def main():
    contacts = load_contacts()

    while True:
        print("\n----- Contact Book -----")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            display_contacts(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            search_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Exiting... All changes have been saved.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
