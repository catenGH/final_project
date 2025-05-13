import pandas as pd 

# cuisine_list = ["African", "Asian", "American", "British", "Cajun", "Caribbean", "Chinese", "Creole", "Eastern European", "European", "French", "German", "Greek", "Indian", "Irish", "Italian", "Japanese", "Jewish", "Korean", "Latin American", "Mediterranean", "Mexican", "Middle Eastern", "Nordic", "Southern", "Spanish", "Thai", "Vietnamese"]
# recipe = pd.read_csv("recipes.csv")

# def cuisine_filter(recipe, selected_filters):
#     filtered_recipes = []

#     for filter in selected_filters:
#         for i, item in recipe.iterrows(): # to iterate through each recipe in the csv, https://www.geeksforgeeks.org/different-ways-to-iterate-over-rows-in-pandas-dataframe/
#             cuisine = item["Cuisine"]
#             if isinstance(cuisine, str):
#                 try:
#                     cuisine_tags = eval(cuisine)
#                     if filter in cuisine_tags:
#                         filtered_recipes.append(i)
#                 except:
#                     continue
    
#     return recipe.loc[filtered_recipes]

def cuisine_filter(recipe, selected_filters, selected_time):
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
    if selected_filters == []:
        new_list = recipe
    else:
        new_list = recipe.loc[filtered_recipes]

    if "<60" in selected_time:
        new_list = new_list.loc[new_list["Cook Time (in minutes)"]<60]
    elif ">=60 & <=120" in selected_time:
        new_list = new_list.loc[(new_list["Cook Time (in minutes)"] >= 60) & (new_list["Cook Time (in minutes)"] < 120)]
    elif ">120" in selected_time:
        new_list = new_list.loc[new_list["Cook Time (in minutes)"]>=120]
    
    return new_list
    

# filter_list = ["Asian"]
# print(cuisine_filter(recipe, filter_list))
recipe = pd.read_csv("recipes.csv")
filter_list = []
selected_time = []
# we can try hard coding each checkbox to match 1, 2, 3 (so like the first option is 1, second option is 2, etc. etc.)

print(cuisine_filter(recipe, filter_list, selected_time))