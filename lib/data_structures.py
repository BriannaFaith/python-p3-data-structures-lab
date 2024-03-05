spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_names= [spice.get("name") for spice in spicy_foods ]
    return spicy_names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [spice for spice in spicy_foods if spice["heat_level"]>5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    print_spicy =[print(f"{spice['name']} ({spice['cuisine']}) | Heat Level: {'🌶'*spice['heat_level']}") for spice in spicy_foods]
    return print_spicy

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spice in spicy_foods:
        if cuisine == spice["cuisine"]:
            return spice


def print_spiciest_foods(spicy_foods):
    for spice in spicy_foods:
        if spice['heat_level'] > 5:
            print(f"{spice['name']} ({spice['cuisine']}) | Heat Level: {'🌶'*spice['heat_level']}")

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(spice["heat_level"] for spice in spicy_foods)
    length=len(spicy_foods)
    average_heat= total_heat_level/length
    return average_heat

def create_spicy_food(spicy_foods, spicy_food):
    new_list = spicy_foods.copy()
    new_list.append(spicy_food)
    return new_list
create_spicy_food(spicy_foods, {
                'name': 'Griot',
                'cuisine': 'Haitian',
                'heat_level': 10,
            },)
