print("COOKING RECIPE HELPER")
ingredients = input("Enter your ingredients: ").lower().split(", ")
time_limit = int(input("How much time d0 you have to cook (in minutes)?"))
if time_limit <= 20:
    suggestions.append("You can make an omelette!")

suggestions = []
if any(ingredients in ["egg" , "bacon", "egg and bacon"] for ingredient in ingredients):
    suggestions.append("you can make egg and bacon!")
if any(ingredients in ["tomatoes", "unions", "broth", "seasoning", "tomatoes, broth, seasoning, unions"] for ingredient in ingredients):
    suggestions.append("You can make tomato soup!")
if any(ingredients in ["bread" , "cheese" , "bread and cheese"] for ingredient in ingredients):
    suggestions.append("You can make grilled cheese")
if any(ingredients in ["carrots" , "bell peppers" , "onions" , "soy sauce" , "garlic"] for ingredient in ingredients):
    suggestions.append("You can make vegetable stir fry!")
if any(ingredients in ["lettuce" , "tomato" , "cucumber" , "dressing"] for ingredient in ingredients):
    suggestions.append("You can make a salad!")
if any(ingredients in ["flour" , "eggs" , "milk" , "sugar" , "butter"] for ingredient in ingredients):
    suggestions.append("You can make pancakes!")
if any(ingredients in ["bread" , "eggs" , "cinnamon" , "sugar" , "butter"] for ingredient in ingredients):
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
    print("Sorry, we dont have a recipe for that combination")
