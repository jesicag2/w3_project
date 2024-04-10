# Project: Contact Management System

import re

contacts = {}

def menu():
    print("\n")
    print ("Welcome to the Contact Management System!\n")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Quit")

def add_contact():
    identifier = input("Enter unique identifier (phone number): ")
    
    if identifier in contacts:
        print("Contact with this information already exists.")
    
    name = input("Enter name: ")

    while True:
        phone_number = input("Enter phone number: ")
        if re.match(r'^\d{10}$', phone_number):
            break
        else:
            print("Seems this is an invalid phone number, please enter a 10-digit number.")

    while True:
        email = input("Enter email address: ")
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            break
        else:
            print("Seems this is an invalid email address, please enter a valid email.")
    
    identifier = phone_number

    contacts[identifier] = {
        "name": name,
        "phone_number": phone_number,
        "email": email,
    }

    print("Contact has been added successfully!") 

def edit_contact():
    identifier = input("Enter unique identifier of the contact you would like to edit: ")
    
    if identifier in contacts:
        name = input("Enter the new name (leave blank to keep the same): ")
        phone_number = input("Enter the new phone number (leave blank to keep the same): ")
        email = input("Enter the new email address (leave blank to keep the same): ")
        
        if name:
            contacts[identifier]['name'] = name
        if phone_number:
            contacts[identifier]['phone_number'] = phone_number
        if email:
            contacts[identifier]['email'] = email
        
        print("Contact updated successfully!")
    else:
        print("Opps, contact not found.")

def delete_contact():
    identifier = input("Enter unique identifier of the contact you would like to delete: ")
    if identifier in contacts:
        del contacts[identifier]
        print("Contact deleted successfully!")
    else:
        print("Opps, contact not found.") 

def search_contact():
    identifier = input("Enter unique identifier of the contact you wish to search: ")
    if identifier in contacts:
        print("Contact information:")
        print(f"Name: {contacts[identifier]['name']}")
        print(f"Phone Number: {contacts[identifier]['phone_number']}")
        print(f"Email: {contacts[identifier]['email']}")
    else:
        print("Opps, contact not found.") 

def display_contacts():
    print("All contacts:")
    for identifier, contact in contacts.items():
        print(f"Identifier: {identifier}")
        print(f"Name: {contact['name']}")
        print(f"Phone Number: {contact['phone_number']}")
        print(f"Email: {contact['email']}")
        print("\n")

def export_contacts():
    pass 

def main():
    while True:
        menu()
        print("\n")

        try:
            option = input("Please select an option (1-7): ")
        
            option = int(option)

            if option in range(1,8):
                if option == 1:
                    add_contact()
                elif option == 2:
                    edit_contact()
                elif option == 3:
                    delete_contact()
                elif option == 4:
                    search_contact()
                elif option == 5:
                    display_contacts()
                elif option == 6:
                    export_contacts()
                else:
                    print("Bye Bye, Have a Nice Day!")
                    break
        
        except ValueError:
            print("Seems you have provided an invalid input, please enter a valid number from 1 to 7.")
        
        # except error as e:

main()