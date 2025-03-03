

print("COOKING RECIPE HELPER")

ingredients = input("Enter your ingredients: ").lower().split()
time_limit = int(input("How much time do you have to cook (in minutes)? "))
time_limit -=5

suggestions = []

if time_limit <= 10:  
    suggestions.append("You can make a smoothie!")  
elif time_limit <= 20:  
    suggestions.append("You can make an omelette!")  
else:  
    suggestions.append("You have time for a full meal!")

recipes = {
    "vegetable stir fry": ["carrots", "bell peppers", "onions", "soy sauce", "garlic"],
    "salad": ["lettuce", "tomato", "cucumber", "dressing"],
    "pancakes": ["flour", "eggs", "milk", "sugar", "butter"],
    "french toast": ["bread", "eggs", "cinnamon", "sugar", "butter"],
    "pizza": ["dough", "cheese", "tomato sauce", "pepperoni", "olives"],
    "chicken soup": ["chicken", "broth", "carrots", "celery", "onions"]
}

for recipe, required_ingredients in recipes.items():  
    if any(ingredient in ingredients for ingredient in required_ingredients):  
        suggestions.append(f"You can make {recipe}!")  
        
if any(ingredient in ["carrots", "bell peppers", "onions", "soy sauce", "garlic"] for ingredient in ingredients):
    suggestions.append("You can make vegetable stir fry!")

if any(ingredient in ["lettuce", "tomato", "cucumber", "dressing"] for ingredient in ingredients):
    suggestions.append("You can make a salad!")

if any(ingredient in ["flour", "eggs", "milk", "sugar", "butter"] for ingredient in ingredients):
    suggestions.append("You can make pancakes!")

if any(ingredient in ["bread", "eggs", "cinnamon", "sugar", "butter"] for ingredient in ingredients):
    suggestions.append("You can make french toast!")

if any(ingredient in ["dough", "cheese", "tomato sauce", "pepperoni", "olives"] for ingredient in ingredients):
    suggestions.append("You can make pizza!")

if any(ingredient in ["eggs", "cheese", "mushrooms", "onions", "peppers"] for ingredient in ingredients):
    suggestions.append("You can make an omelette!")

if any(ingredient in ["chicken", "broth", "carrots", "celery", "onions"] for ingredient in ingredients):
    suggestions.append("You can make chicken soup!")

if suggestions:
    for suggestion in suggestions:
        print(suggestion)
else:
    print("Sorry, we don't have a recipe for that combination")