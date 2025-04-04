'''
I've programmed this prototype/demo to run through all of our functions and print explanations for them. 
'''

import requests
import json
import csv
import time
from get_ingredientlist import get_ingr_list
from search_recipes import search_recipes
from get_cookinglevel import get_cooklevel

print("Welcome to our prototype! This will show the various functions we've created and explain how we plan to use them!")
print("We've also used the time module to spread out print statements for readability.")
time.sleep(5)
print("Our first function can be used to get a list of ingredients. We can use this to create a set of ingredients a user can chose from.")
print("This function returns the following list:")
time.sleep(5)
print(get_ingr_list())
time.sleep(2)

print("This next function searches for recipes based on user-selected ingredients, and stores these recipies in a csv.")
print("Test it out now!")

ingredient_list = []
ingredient = input("Give us an ingredient:")
ingredient_list.append(ingredient)
while True:
    users_input = input("Do you want to add another ingredient to your list? y/n: ").lower()
    if users_input == "y":
        ingredient = input("Add an ingredient: ").lower()
        ingredient_list.append(ingredient)
    elif users_input == "n":
        break
    else:
        print("Please enter 'y' or 'n'!")

print(f"Okay! We will now search for recipes for the following ingredients: {ingredient_list}")
search_recipes(ingredient_list)
time.sleep(2)
print("Done! The results are stored in the csv titled 'recipes.csv'")
print("This csv holds multiple pieces of info on eache recipe returned from the api, and will be used to show results on the front end.")
time.sleep(4)

print("Our next function takes an input of cooking time and returns a skill level assignment.")
print("We plan to later use this to filter recipies by cook time/skill level.")
while True:
    usr_input = input("How much time do you usually have to cook, on average (in minutes)?")
    if usr_input.isalpha():
        print("Please enter a number!")
    else:
        break
cooking_level = get_cooklevel(int(usr_input))
print(f"Based on your answer, we've determined that your cooking level is {cooking_level}!")


