# Question 1

person = {
    'first_name': 'Tom',
    'last_name': 'Jerry',
    'age': '19',
    'city': 'New York'
}
print("Tom's last name is " + person['last_name'] +
      "\nHe is " + person['age'] + " years old and lives in " + person['city'] + ".")

# Question 2
print("------------------------------------------")

favorite_food = {
    'John': "Macaroni and Cheese",
    'Mike': "Steak with side salad",
    'Dorj': "Vegetable Soup",
    'Tuya': "Milk tea with dumplings",
    'Haliun': "Cherry Pie",
    }

for key in favorite_food.keys():
    print(key + "'s favorite food is " + str(favorite_food[key]))
pets = []
pet = {
    'name': 'Hund',
    'owner': 'Karl',
    'type': 'Dog',
    'breed': 'Great Dane',
    'age': '3 years old',
    'color': 'brindle',
}
pets.append(pet)

pet = {
    'name': 'Neko',
    'owner': 'Erdene',
    'type': 'Cat',
    'breed': 'Maine Coon',
    'age': '38 months',
    'color': 'black',
}
pets.append(pet)

pet = {
    'name': 'Hama',
    'owner': 'Jess',
    'type': 'Pigeon',
    'breed': 'Dove',
    'age': '7 months',
    'color': 'white',
}
pets.append(pet)

for pet in pets:
    print("\nThis is my pet " + pet['name'] + " and all i know about it's: ")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
