import requests
import json

#Creates an ingredient list based on what mealDB has
def get_ingr_list():
    ingredients_api = requests.get("https://www.themealdb.com/api/json/v1/1/list.php?i=list").json()
    ingredients_dict = ingredients_api["meals"]
    ingredients_dict

    ingredients_list = []

    for ingredient in ingredients_dict:
        name = ingredient["strIngredient"]
        ingredients_list.append(name.lower())

    return(ingredients_list)

get_ingr_list()