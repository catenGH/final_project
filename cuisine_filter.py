import pandas as pd 

cuisine_list = ["African", "Asian", "American", "British", "Cajun", "Caribbean", "Chinese", "Creole", "Eastern European", "European", "French", "German", "Greek", "Indian", "Irish", "Italian", "Japanese", "Jewish", "Korean", "Latin American", "Mediterranean", "Mexican", "Middle Eastern", "Nordic", "Southern", "Spanish", "Thai", "Vietnamese"]
recipe = pd.read_csv("recipes.csv")

def cuisine_filter(recipe):
    cuisine_input = input(f"What cuisine do you want to filter for?: {cuisine_list}")
    filtered_recipes = []

    for i, item in recipe.iterrows(): # to iterate through each recipe in the csv, https://www.geeksforgeeks.org/different-ways-to-iterate-over-rows-in-pandas-dataframe/
        cuisine = item["Cuisine"]
        if isinstance(cuisine, str):
            try:
                cuisine_tags = eval(cuisine)
                if cuisine_input in cuisine_tags:
                    filtered_recipes.append(i)
            except:
                continue
    
    if filtered_recipes:
        return recipe.loc[filtered_recipes]
    else:
        return "No recipes found"

print(cuisine_filter(recipe))