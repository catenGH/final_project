import pandas as pd 

cuisine_list = ["African", "Asian", "American", "British", "Cajun", "Caribbean", "Chinese", "Creole", "Eastern European", "European", "French", "German", "Greek", "Indian", "Irish", "Italian", "Japanese", "Jewish", "Korean", "Latin American", "Mediterranean", "Mexican", "Middle Eastern", "Nordic", "Southern", "Spanish", "Thai", "Vietnamese"]
recipe = pd.read_csv("recipes.csv")

def cuisine_filter(recipe, selected_filters):
    filtered_recipes = []

    for filter in selected_filters:
        for i, item in recipe.iterrows(): # to iterate through each recipe in the csv, https://www.geeksforgeeks.org/different-ways-to-iterate-over-rows-in-pandas-dataframe/
            cuisine = item["Cuisine"]
            if isinstance(cuisine, str):
                try:
                    cuisine_tags = eval(cuisine)
                    if filter in cuisine_tags:
                        filtered_recipes.append(i)
                except:
                    continue
    
    return recipe.loc[filtered_recipes]

filter_list = ["Asian"]
print(cuisine_filter(recipe, filter_list))