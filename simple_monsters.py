import string
monster_name = input("Enter monster name: ")
with open('monsters_simple.txt', 'r') as file:
    for line in file:
        name, description = line.strip().split(',', 1)
        if name.lower() == monster_name.lower():
            print(f"Name: {name}\nDescription: {description}")
