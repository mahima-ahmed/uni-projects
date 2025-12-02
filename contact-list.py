# Develop a program that simulates a contact agenda. Contacts will be stored in a dictionary, where the keys are contact names and the values are lists containing the phone number, email, and address. The program should allow the following operations:
# 1. Add a contact with name, phone number, email, and address.
# 2. Modify a contact’s information (for example, change the phone number or email of an existing contact).
# 3. Delete a contact by name.
# 4. Search for a contact by name and display their information.
# 5. List all stored contacts.
# 6.Exit the program.

# Part 1 - Add a contact: with name, phone number, email address, address.
def add_contact(name: str, phone_number: str, email_address: str, address: str, contact_list: dict) -> None:
    if name in contact_list:
        print('The contact name already exists.')
    else:
        contact_list[name] = [phone_number, email_address, address]
        print('The contact has been added successfully.')

# Part 2 - Modify a contact's details (e.g. change the number/email of an existing contact).
def modify_contact(name: str, phone_number: str, email_address: str, address: str, contact_list: dict) -> None:
    if name in contact_list:
        contact_list[name] = [phone_number, email_address, address]
        print('The contact has been modified successfully.')
    else:
        print('The contact does not exist.')

# Part 3 - Delete a contact by name.
def delete_contact(name: str, contact_list: dict) -> None:
    if name in contact_list:
        del contact_list[name]
        print ('The contact name has been deleted successfully')
    else:
        print ('The contact does not exist and cannot be deleted.')

# Part 4 - Search a contact by name and show their data.
def search_contact(name: str, contact_list: dict) -> None:
    if name in contact_list:
        data = contact_list[name]
        print ('Contact Details:')
        print ('Phone Number: ', data[0])
        print('Email Address: ', data[1])
        print('Address: ', data[2])
    else:
        print('The contact does not exist and cannot be searched.')

# Part 5 - List all stored contacts.
def print_contact(contact_list: dict) -> None:
    if len(contact_list) == 0:
        print("There are no contacts registered.")
    else:
        print ('--- CONTACT LIST ---')
        for name, data in contact_list.items():
            data = contact_list[name]
            print (f"{name} - Phone: {data[0]}, Email: {data[1]}, Address: {data[2]}")

seguir = True
while seguir:
    print("--- CONTACT LIST ---")
    print("1. Add a contact")
    print("2. Modify a contact")
    print("3. Delete a contact")
    print("4. Search a contact")
    print("5. List all contacts")
    print("6. Exit")

    option = input("Choose an option: ")

    if option == "1":
        name = input("Name: ")
        phone_number = input("Phone Number: ")
        email_address = input("Email Address: ")
        address = input("Address: ")
        add_contact(name, phone_number, email_address, address, contact_list)
    elif option == "2":
        name = input("Enter the name of the contact to modify: ")
        phone_number = input("New Phone Number: ")
        email_address = input("New Email Address: ")
        address = input("New Address: ")
        modify_contact(name, phone_number, email_address, address, contact_list)
    elif option == "3":
        name = input("Enter the name of the contact to delete: ")
        delete_contact(name, contact_list)
    elif option == "4":
        name = input("Name: ")
        search_contact(name, contact_list)
    elif option == "5":
        print_contact(contact_list)
    elif option == "6":
        print("Exiting...")
        break

    else:
        print("Invalid option. Try again, please.")
