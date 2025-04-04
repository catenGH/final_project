import requests
import json
import csv


#usr_ingr should be a list of the ingredients a user submits
#Creates a csv of recipes
def search_recipes(usr_ingr):
    csv_file = open("recipes.csv", "w", newline="", encoding="utf-8")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Recipe Name", "Thumbnail Link", "Cook Time", "Recipe Source"])

    key = "5cb09004fe27449689868405b5a33789"
    search = requests.get(f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={usr_ingr}&apiKey={key}").json()

    for recipe in search:
        id_num = recipe["id"]
        recipe_info = requests.get(f"https://api.spoonacular.com/recipes/{id_num}/information?apiKey={key}").json()
        recipe_name = recipe_info["title"]
        recipe_pic = recipe_info["image"]
        cook_time = recipe_info["readyInMinutes"]
        recipe_time = f"{cook_time} minutes"
        recipe_source = recipe_info["sourceUrl"]
        csv_writer.writerow([recipe_name, recipe_pic, recipe_time, recipe_source])
    csv_file.close()

list = ["chicken", "onion"]
search_recipes(list)

