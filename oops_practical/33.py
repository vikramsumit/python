# Design a base class "Food" with a method prepare_recipe() that prints a generic message like "Follow the standard recipe steps." Create derived classes for different types of dishes, such as "Pizza," "Pasta," and "Salad." Override the prepare_recipe() method in each derived class to provide specific preparation steps for that dish. 

class Food:
    def prepare_recipe(self):
        print("Follow the standard recipe steps.")

class Pizza(Food):
    def prepare_recipe(self):
        print("Follow these steps to prepare pizza: \n1. Preheat oven to 475°F.\n2. Spread tomato sauce on dough.\n3. Add cheese and toppings.\n4. Bake for 15 minutes.\n")

class Pasta(Food):
    def prepare_recipe(self):
        print("Follow these steps to prepare Pasta: \n1. Boil water. \n2. Cook pasta al dente. \n3. Sauté garlic and sauce. \n4. Mix and serve.\n")

class Salad(Food):
    def prepare_recipe(self):
        print("FOllow these steps to Prepare Salad: \n1. Chop vegetables. \n2. Mix with dressing. \n3. Add proteins if desired. \n4. Toss and serve cold.\n")

pizza = Pizza()
pasta = Pasta()
salad = Salad()

pizza.prepare_recipe()
pasta.prepare_recipe()
salad.prepare_recipe()