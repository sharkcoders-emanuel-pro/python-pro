# Functions

def get_contact(contacts ,name):
    return contacts[name]

def register_contact(contacts, name, number):
    if number not in contacts:
        contacts[name] = number
    else:
        print("The contact already exists.")

def remove_contact(contacts, name):
    contacts.pop(name)

def list_contacts(contacts):
    return contacts

# Menu

contacts = {'Eduardo' : 963852741,
            'Emanuel' : 987654321,
            'Alberto' : 951741357}

print("1 - Listar Contacto")
print("2 - Adicionar Contacto")
print("3 - Remover Contacto")
print("4 - Apresentar Contactos")

option = int(input("> "))

if option == 1:
    name = input("Please insert the name of the contact: ")
    print(get_contact(contacts, name))

elif option == 2:
    name = input("Please insert the name of the contact: ")
    phone_number = int(input("Please insert the name of the contact: "))
    register_contact(contacts, name, phone_number)
    print("The contact was successfully added!")
    print(list_contacts(contacts))

elif option == 3:
    name = input("Please insert the name of the contact: ")
    remove_contact(contacts, name)
    print("The contact was successfully removed!")
    print(list_contacts(contacts))

elif option == 4:
    print(list_contacts(contacts))

else:
    print("Opção inválida!")