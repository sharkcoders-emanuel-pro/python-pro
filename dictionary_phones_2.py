# Functions

def get_contact(contacts,name):
   return contacts.get(name,"Contact not Found.")

def register_contact(contacts,name,number):
    if name in contacts:
        return "The contact already exists."
    elif number in contacts.values():
        return "The contact Number already exists."
    else:
        contacts[name] = number
        return "The contacts successfully added."

def remove_contact(contacts, name):
    if name in contacts:
        contacts.pop(name)
        return "The contact was successfully removed."
    else:
        return "The contact does not exist."


def list_contacts(contacts):
    return contacts

# Menu

def main_menu():
    print("1 - Show Contact")
    print("2 - Add Contact")
    print("3 - Remove Contact")
    print("4 - Show Contacts")
    print("5 - Close")
    option = int(input("Select your Option: "))
    return option

def main():

    contacts = {'Emanuel': 986220785,
              'Eduardo': 985220689,
              'Joel': 9842256781}

    option = 0

    while option != 5:

        option = main_menu()

        if option == 1:
            name = input("Please insert the name of the contact: ")
            print(get_contact(contacts, name))

        elif option == 2:
            name = input("Please insert the name of the contact: ")
            phone_number = int(input("Please insert the number of the contact: "))
            result = register_contact(contacts, name, phone_number)
            print(result)
            print(list_contacts(contacts))

        elif option == 3:
            name = input("Please insert the name of the contact: ")
            result = remove_contact(contacts, name)
            print(result)
            print(list_contacts(contacts))

        elif option == 4:
            print(list_contacts(contacts))

        elif option == 5:
            print("Sair")

        else:
            print("Invalid Option!")


if __name__ == '__main__':
    main()

