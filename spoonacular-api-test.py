import requests
import json

#To have a key you need an account- for this project I made an account so we can share this key
#We are also limited by a free account, meaning 1 req/second + 150 max req per day
#Note - Put this at the end of an api call
key = "&apiKey=6eccbe1676054b1e9304c8d1f5225764"

'''
GENERAL SYNTAX:
Base link: https://api.spoonacular.com

Most of our searches will be for recipies, making the url:
https://api.spoonacular.com/recipies/(request type)?(parameter)&(parameter)&(parameter)
Note that the first parameter has a "?" before it, and every following parameter is separated by "&"

'''

#Following are some tests. To see the results of each, uncomment the print statement.
#I specifically picked ones that could be useful to us

#Complex search - can use a query to search for a type of dish, as well as add cuisine and diet (and many others)
#https://spoonacular.com/food-api/docs#Search-Recipes-Complex
complexsearch_test = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?query=pasta{key}").json()
# print(json.dumps(complexsearch_test, indent=4))

#Find By Ingredients - Takes a list of ingredients (IN A STRING, NOT PYTHON LIST) separated by a comma and searches
#https://spoonacular.com/food-api/docs#Search-Recipes-by-Ingredients 
ingr = "apples,flour,sugar"
find_ingredients_test = requests.get(f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingr}{key}").json()
print(json.dumps(find_ingredients_test, indent=4))

'''
Overall the documentation is extremely straightforward and everything follows the same logic as above.
If you want me to test out any other specific functions from the documentation (there's over 100, and quite a few we can use for this project) lmk!
- Corey
'''