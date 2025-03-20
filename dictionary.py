# Aulas 11 - Dictionary in Python

# Syntax {key:value}

dictionary = {'name' : "Emanuel", 'age' : 30, 'description' : "Student of Python Pro"}

# Print value from dictionary
print(f"Name: {dictionary['name']} | Age: {dictionary['age']} | Description : {dictionary['description']}")



# Example Movies


movies = {'Star Wars' : 1977, 'Titanic' : 1997}

print(f"Movies\n"
    f"Star Wars: {movies['Star Wars']}\n"
    f"Titanic: {movies['Titanic']}")


# Add Another Movie

movies['Scarface'] = 1983

print(f"Scarface: {movies['Scarface']}")

# Add more than one Movie at the same time



movies['Iron Man'] = 2008
movies['Iron Man 2'] = 2010
movies['The Avengers'] = 2012

print(f"Iron Man: {movies['Iron Man']}")
print(f"Iron Man 2: {movies['Iron Man 2']}")
print(f"The Avengers: {movies['The Avengers']}\n\n")


# Remove a Movie


movies.pop('Titanic')

print(movies)


# varify length of a dictionary


print(len(movies))


# Verify if a movie is or not in the dictionary

if 'Star Wars' in movies:
    print("Yes, this movies is in the dictionary.")

else:
    print("No, this movies isn't the dictionary.")


if 'Lord of the Ring' in movies:
    print("Yes, this movies is in the dictionary.")

else:
    print("No, this movies isn't the dictionary.")



# Verify if a movie is Not in the dictionary

if 'Star Wars' in movies:
    print("No, this movies isn't the dictionary.")

else:
    print("Yes, this movies is in the dictionary.")


if 'Lord of the Ring' in movies:
    print("No, this movies isn't the dictionary.")

else:
    print("Yes, this movies is in the dictionary.")








