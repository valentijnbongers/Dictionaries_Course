import json
import random # This will be us

# Load the JSON file
with open('names.json', 'r') as file:
    names_dict = json.load(file)

for name, details in names_dict.items():
    print(f"Name: {name}")
    print(f"  Gender: {details['gender']}")
    print(f"  Country: {details['country']}")
    print()  # Print a blank line for better readability
random_names = {}
names = list(names_dict)
for i in range(1,21):
    current_name = random.choice(names)
    if current_name in random_names:
        break
    else:
        random_names[current_name] = names_dict[current_name]
count = 1
for name in random_names:
    name_dict = random_names[name]
    print(f"{count}. {name}")
    print("Gender: ", name_dict['gender'])
    print("Country:", name_dict['country'])
    print('')
    count = count + 1
