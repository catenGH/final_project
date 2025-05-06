import requests
import json
import csv

def search_recipes(ingredient_list):
    csv_file = open("recipes.csv", "w", newline="", encoding="utf-8")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Recipe Name", "Thumbnail Link", "Ingredients", "Cook Time (in minutes)", "Diet", "Cuisine", "Recipe Source"])

    # Corey's Key: 6eccbe1676054b1e9304c8d1f5225764 
    # Cates's Key: 5cb09004fe27449689868405b5a33789

    key = "5cb09004fe27449689868405b5a33789"

    format_ingr_list = ",+".join(ingredient_list)
    find_ingredients = requests.get(f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={format_ingr_list}&apiKey={key}")
    ingredients_json = find_ingredients.json()
    for recipe in ingredients_json:
        id_num = recipe["id"]
        recipe_info = requests.get(f"https://api.spoonacular.com/recipes/{id_num}/information?apiKey={key}").json()
        recipe_name = recipe_info["title"]
        recipe_pic = recipe_info["image"]
        cook_time = recipe_info["readyInMinutes"]
        recipe_diets = recipe_info["diets"]
        if recipe_info["cuisines"]:
            recipe_cuisine = recipe_info["cuisines"]
        else:
            recipe_cuisine = "NaN"
        ingredients_list = []
        for i in recipe_info["extendedIngredients"]:
            ingredient_name = i["nameClean"]
            ingredients_list.append(ingredient_name)
        recipe_source = recipe_info["sourceUrl"]
        csv_writer.writerow([recipe_name, recipe_pic, ingredients_list, cook_time, recipe_diets, recipe_cuisine, recipe_source])
    csv_file.close()

# ingr_list = ["chicken", "onion"]

# search_recipes(ingr_list)



     


