# Functions

def get_contact(contacts,name):
   return contacts[name]

def register_contact(contacts,name,number):
    if number not in contacts:
        contacts[name] = number
    else:
        print("The contact already exists.")

def remove_contact(contacts, name):
    contacts.pop(name)

def list_contacts(contacts):
    return contacts

# Menu


phones = {'Emanuel' : 986220785,
          'Eduardo' : 985220689,
          'Joel' : 9842256781}

def main_menu():
    print("1 - Listar Contactos")
    print("2 - Adicionar Contactos")
    print("3 - Remover Contactos")
    print("4 - Apresentar Contactos")
    print("5 - Sair")
    option = int(input("Introduza aqui a opçao que Pretende: "))
    return option



def main():

    option = 0
    while option != 5:
        option = main_menu()
        if option == 1 :
            name = input("Please insert the name of the contact: ")
            print(get_contact(contacts, name))

        elif option == 2 :
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

        elif option == 5:
            print("Sair")

        else:
            print("Opção inválida!")




name = input("Insert the name of the Contact you Want: ")
print(f"The Number is: {get_contact(name)}")