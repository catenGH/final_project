import requests
import json

#Reminder: Get ingredient list from other function
#May not use in final in favor of spoonacular
def ingredient_input(main_ingr, ingr_list):
    if main_ingr in ingr_list:
        main_ingr = main_ingr.replace(" ", "_")
        meal_api = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?i={main_ingr}")
        meal_json = meal_api.json()
        results = {}
        for meal in meal_json["meals"]:
            meal_name = meal.get("strMeal")
            meal_ID = meal.get("idMeal")
            recipe_api = requests.get(f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_ID}")
            recipe_json = recipe_api.json()
            if recipe_json.get("meals"):
                recipe_ingredients = []
                recipe_pic = recipe_json["meals"][0]["strMealThumb"]
                recipe_instructions = recipe_json["meals"][0]["strInstructions"].replace("\r\n", " ")
                recipe = recipe_json["meals"][0]["strSource"]
                for key in recipe_json["meals"][0]:
                    if "strIngredient" in key:
                        ingredient_name = recipe_json["meals"][0][key]
                        if ingredient_name:
                            recipe_ingredients.append(ingredient_name)
                        else:
                            continue
                results[meal_name] = [recipe_pic, recipe_ingredients, recipe_instructions, recipe]
        return(results)
    else:
        return("We don't have this, pick something else!")

list = ["chicken"]
print(ingredient_input("chicken", list))
