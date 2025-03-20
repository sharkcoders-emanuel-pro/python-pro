def get_contacts(name):
   return phones[name]


phones = {'Emanuel' : 986220785,
          'Eduardo' : 985220689,
          'Joel' : 9842256781}

name = input("Insert the name of the Contact you Want: ")
print(f"The Number is: {get_contacts(name)}")



