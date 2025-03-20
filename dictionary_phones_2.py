# Functions

def get_contact(contacts,name):
   return contacts[name]

def set_contact(contacts,name,phone_number):
    contacts[name] = phone_number

def remove_contact(contacts,name):
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
        if(option == 1):
            print(f"{set_contacts(name)}")



name = input("Insert the name of the Contact you Want: ")
print(f"The Number is: {get_contacts(name)}")