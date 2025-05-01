import tkinter as tk
from tkinter import ttk
import requests
from PIL import ImageTk, Image
from io import BytesIO



import requests
import json
import csv
import pandas as pd

#---------------

#usr_ingr should be a list of the ingredients a user submits
#Creates a csv of recipes
def search_recipes(usr_ingr):
    csv_file = open("recipes.csv", "w", newline="", encoding="utf-8")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Recipe Name", "Thumbnail Link", "Cook Time", "Recipe Source"])

    key = "6eccbe1676054b1e9304c8d1f5225764"
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

#--------------------

root = tk.Tk()
root.title("Fridge to Food")

mainframe = tk.Frame(root)
mainframe.pack(fill="both", expand=True)

heading = tk.Frame(mainframe, bg="mediumorchid3")
heading.pack(side="top", fill="x")

response = requests.get("https://i.postimg.cc/tCLRtKB7/logo-1.png")
image_info = BytesIO(response.content)
logo_img = Image.open(image_info)
logo_img.thumbnail((200, 200))
logo = ImageTk.PhotoImage(logo_img)
panel = tk.Label(heading, image=logo, bg="mediumorchid3")
panel.image = logo
panel.pack(side="left", padx=20)

# title = tk.Label(heading, text="Fridge to Food", font=("Helvetica 24 bold", 20, "bold"), bg="mediumorchid3", fg="white", anchor="w")
# title.pack(side="left", padx=20)

search = tk.Button(heading, text="🔎", highlightbackground="mediumorchid3")
search.pack(side="right", padx=20)

add_ingredient = tk.Button(heading, text="✚", highlightbackground="mediumorchid3")
add_ingredient.pack(side="right", padx=10)

ingredient = tk.StringVar()
ingredients_input = tk.Entry(heading, textvariable=ingredient, width=50)
ingredients_input.pack(side="right")

subheading = tk.Frame(mainframe, bg="light gray")
subheading.pack(side="top", fill="x")

instructions = tk.Label(subheading, text="Welcome to Fridge to Food!  Search for ingredients, add the ingredients in your fridge by using ✚, and search for recipes by pressing 🔎!", bg="light gray")
instructions.pack(pady=5)

other_stuff = tk.Label(subheading, text="Each recipe will contain a picture as well as information about its cooktime, ingredients, cuisine, diet, and allergens!", bg="light gray")
other_stuff.pack(pady=5)

more_instructions = tk.Label(subheading, text="↙ You can also filter for specific cook times and cuisines!", bg="light gray")
more_instructions.pack(pady=5)

filters = tk.Frame(mainframe, bg="gray", width=200)
filters.pack(side="left", padx=10, pady=10, fill="y")

cooktime = tk.Frame(filters, bg="gray")
cooktime.pack(padx=10, pady=10)

cooktime_title = tk.Label(cooktime, text="Cook Time (in minutes)", bg="gray", fg="white")
cooktime_title.pack()

cooktimes = ["<60", ">=60 & <=120", ">120"]
for time in cooktimes:
    cooktime_filter = tk.Checkbutton(cooktime, text=time, bg="gray")
    cooktime_filter.pack()

cuisines = tk.Frame(filters, bg="gray")
cuisines.pack(padx=10, pady=10)

cuisines_label = tk.Label(cuisines, text="Cuisines", bg="gray", fg="white")
cuisines_label.pack()

cuisine_list = ["African", "Asian", "American", "British", "Cajun", "Caribbean", "Chinese",
                "Eastern European", "European", "French", "German", "Greek", "Indian", "Irish", "Italian",
                "Japanese", "Jewish", "Korean", "Latin American", "Mediterranean", "Mexican",
                "Middle Eastern", "Nordic", "Southern", "Spanish", "Thai", "Vietnamese"]

for i in cuisine_list:
    cuisine = tk.Checkbutton(cuisines, text=i, bg="gray")
    cuisine.pack()

recipes = tk.Frame(mainframe, bg="white")
recipes.pack(fill="both", padx=10, pady=10)

recipe_heading = tk.Label(recipes, text="Recipes", font=(20), bg="white")
recipe_heading.pack()

# recipe_examples = {["Recipe 1", "picture", "20 minutes", "vegan", "Mediterranean", "chickpeas, lentils, paprika", "random website"],
#                    ["Recipe 2", "picture", "10 minutes", "none", "Chinese", "pork belly, soy sauce, sugar", "other website"]}

# #NOTE NOTE NOTE NOTE
# def search_recipes(usr_ingr):
#     csv_file = open("recipes.csv", "w", newline="", encoding="utf-8")
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(["Recipe Source", "Recipe Name", "Thumbnail Link", "Cook Time",])

#     key = "6eccbe1676054b1e9304c8d1f5225764"
#     search = requests.get(f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={usr_ingr}&apiKey={key}").json()

#     for recipe in search:
#         id_num = recipe["id"]
#         recipe_info = requests.get(f"https://api.spoonacular.com/recipes/{id_num}/information?apiKey={key}").json()
#         recipe_name = recipe_info["title"]
#         recipe_pic = recipe_info["image"]
#         cook_time = recipe_info["readyInMinutes"]
#         recipe_time = f"{cook_time} minutes"
#         recipe_source = recipe_info["sourceUrl"]
#         csv_writer.writerow([recipe_source, recipe_name, recipe_pic, recipe_time])
#     csv_file.close()

# list = ["chicken", "onion"]
# search_recipes(list)

data = pd.read_csv("recipes.csv")

recipe_list = data["Recipe Name"].tolist()
img_list = data["Thumbnail Link"].tolist()

def load_img(url):
    response = requests.get(url)
    img_info = BytesIO(response.content)
    pil_img = Image.open(image_info)
    return ImageTk.PhotoImage(pil_img)

def show_img(url):
    global img_refrence
    pil_img = load_img(url)
    if pil_img is not None:
        recipe_img.delete("all")
        recipe_img.create_image(300, 300, anchor="center", image=pil_img)
        img_refrence = pil_img

for i in recipe_list:
    img = 0

    recipe_box = tk.Frame(recipes, bg="gray", bd=2, padx=10, pady=10)
    recipe_box.pack(side="left", padx=10, pady=10)
    recipe_title = tk.Label(recipe_box, text=i, bg="gray")
    recipe_img = tk.Canvas(recipe_box, width=300, height=300, bg="white")
    show_img(img_list[img])

    recipe_img.pack()
    recipe_title.pack(anchor="w")
    print(img_list[img])
    img+=1


# figure out why scrollbar isn't working
filter_scroll = tk.Scrollbar(filters, orient="vertical")
filter_scroll.pack(side="right", fill="y")

root.mainloop()