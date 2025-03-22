# Present by key (alphabetic order)
movies = {'Star Wars' : 1977, 'Titanic' : 1997, 'Jurassic Park': 1993}
print(sorted(movies))

print("\n")

# Present by value (numeric order)
for x in sorted(movies.items()):
    print(f"The Movie {x[0]} is from the Year {x[1]}")

