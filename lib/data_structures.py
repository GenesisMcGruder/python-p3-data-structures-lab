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
    spicy_names = [food.get("name") for food in spicy_foods]
    return spicy_names

def get_spiciest_foods(spicy_foods):
    spice_level = [food for food in spicy_foods if food.get("heat_level") > 5]
    return spice_level

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        heat_level = "🌶" * spicy_food["heat_level"]
        print(f'{spicy_food["name"]} ({spicy_food["cuisine"]}) | Heat Level: {heat_level}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if cuisine == food["cuisine"]:
            return food

def print_spiciest_foods(spicy_foods):
    for spicy_food in spicy_foods:
        if spicy_food["heat_level"] >= 5:
            print_spicy_foods([spicy_food])

def get_average_heat_level(spicy_foods):
    spice_level = [food.get("heat_level") for food in spicy_foods]
    avg_spice = sum(spice_level)/len(spice_level)
    return avg_spice

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
