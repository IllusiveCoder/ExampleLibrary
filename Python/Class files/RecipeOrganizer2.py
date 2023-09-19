import json

'''Description: This program helps users organize their favorite 
recipes. Users can add recipes with ingredients and instructions, 
view recipes, and search for specific recipes. 
The program stores recipe data in a JSON file.'''

class RecipeOrganizer:
    def __init__(self, filename):
        self.filename = filename
        self.recipes = {}

    def add_recipe(self, name, ingredients, instructions):
        self.recipes[name] = {"ingredients": ingredients, "instructions": instructions}
        self.save_to_file()

    def save_to_file(self):
        with open(self.filename, "w") as file:
            json.dump(self.recipes, file, indent=4)

    def load_from_file(self):
        try:
            with open(self.filename, "r") as file:
                self.recipes = json.load(file)
        except FileNotFoundError:
            pass

    def view_recipe(self, name):
        recipe = self.recipes.get(name)
        if recipe:
            print(f"Recipe: {name}")
            print("Ingredients:")
            for ingredient in recipe["ingredients"]:
                print(f"- {ingredient}")
            print("Instructions:")
            for step, instruction in enumerate(recipe["instructions"], start=1):
                print(f"{step}. {instruction}")
        else:
            print(f"Recipe '{name}' not found.")

# Usage example
recipe_organizer = RecipeOrganizer("recipes.json")
recipe_organizer.add_recipe("Spaghetti Bolognese", ["200g spaghetti", "400g ground beef", "1 can tomatoes"], ["1. Boil spaghetti.", "2. Brown beef in a pan.", "3. Add tomatoes and simmer."])
recipe_organizer.load_from_file()
recipe_organizer.view_recipe("Spaghetti Bolognese")
