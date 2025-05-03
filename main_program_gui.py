'''
TO DO:
- Add more info to recipe cards
- Click recipe cards to go to recipe
- Connect filters 
'''

#Imports
from tkinter import ttk
import tkinter as tk
import requests
from PIL import ImageTk, Image
from io import BytesIO
import pandas as pd

#Function Imports from py files
from search_recipes import search_recipes

#Main Setup
root = tk.Tk()
root.title("Fridge to Food")

mainframe = tk.Frame(root)
mainframe.pack(fill="both", expand=True)

heading = tk.Frame(mainframe, bg="mediumorchid3")
heading.pack(side="top", fill="x")   

#Logo
response = requests.get("https://i.postimg.cc/tCLRtKB7/logo-1.png")
image_info = BytesIO(response.content)
logo_img = Image.open(image_info)
logo_img.thumbnail((200, 200))
logo = ImageTk.PhotoImage(logo_img)
panel = tk.Label(heading, image=logo, bg="mediumorchid3")
panel.image = logo 
panel.pack(side="left", padx=20)

#Ingredient Input
ingredient_list = []

#Ref list makes sure pillow does not forget images and displays them properly
img_ref_list = []

#Adds ingredient to above list and deletes input from the textbox
def add_ingr(ingr):
    ingredient_list.append(ingr)
    ingredients_input.delete(0, "end")

def search_display(ingr_list):
    #Uses search recipe function and displays the recipes returned

    #NOTE: Comment out this when not testing search
    # search_recipes(ingr_list)

    #Pandas CSV functions converting necessary data to lists 
    data = pd.read_csv("recipes.csv")

    recipe_list = data["Recipe Name"].tolist()
    img_list = data["Thumbnail Link"].tolist()
    diet_list = data["Diet"].tolist()

    #Global variables to iterate through the images, diets, and frames properly
    itr = 0
    rec_row = 1
    rec_col = 0

    #rec stands for recipe
    for rec in recipe_list:
        #If there's already 3 in a row, move down a row (so that way all recipes will fit on most screens)
        #NOTE: Cate, let me know if this looks good on your end, thanks! -Corey
        if rec_col == 3:
            rec_col = 0
            rec_row += 1

        img_link = img_list[itr]

        recipe_box = tk.Frame(recipes_inner_frame, bg="gray", bd=2, padx=10, pady=10)
        recipe_title = tk.Label(recipe_box, text=rec, font=('Helvetica',12, "bold"), bg="gray", fg="white")
        recipe_canvas = tk.Canvas(recipe_box, width=300, height=300, bg="white")
        recipe_canvas.pack()
        recipe_title.pack(anchor="w")
        
        #Img display, will display a default canvas if img doesn't work
        try:
            #Gets image and adds it to canvas
            response = requests.get(img_link)
            info = BytesIO(response.content)
            image = Image.open(info)
            pil_img = ImageTk.PhotoImage(image)
            recipe_canvas.create_image(150, 150, anchor="center", image=pil_img)

            #Very important to keep this, otherwise PIL will forget the images and not display them!!
            img_ref_list.append(pil_img)
        except:
            recipe_canvas.create_text(150, 150, text="No Image :(", fill="black")

        #Diets Display
        #Diets that will display:
        disp_diet_list = ["vegan", "vegetarian", "gluten free", "dairy free"]

        for diet in disp_diet_list:
            if diet in diet_list[itr]:
                diet_label = tk.Label(recipe_box, text=f"{diet} ✔", bg="gray")

            else:
                diet_label =tk.Label(recipe_box, text=f"{diet} ✘", bg="gray")
            
            diet_label.pack(anchor="w")

        recipe_box.grid(row=rec_row,column=rec_col, padx=10, pady=10)

        #Iterates through images + columns
        itr+=1
        rec_col += 1
    
    #Clears ingredient list after searching
    ingredient_list = []

search = tk.Button(heading, text="🔎", highlightbackground='mediumorchid3',
                   command=lambda: search_display(ingredient_list))
search.pack(side="right", padx=20)

add_ingredient = tk.Button(heading, text="✚",highlightbackground='mediumorchid3',
                           command=lambda: add_ingr(ingredient.get()))
add_ingredient.pack(side="right", padx=10)

ingredient = tk.StringVar()
ingredient.set("")

ingredients_input = tk.Entry(heading, textvariable=ingredient, width=50)
ingredients_input.pack(side="right")

subheading = tk.Frame(mainframe, bg="light gray")
subheading.pack(side="top", fill="x")

#Instruction Labels
instructions = tk.Label(subheading, text="Welcome to Fridge to Food!  Search for ingredients, add the ingredients in your fridge by using ✚, and search for recipes by pressing 🔎!", bg="light gray")
instructions.pack(pady=5)

other_stuff = tk.Label(subheading, text="Each recipe will contain a picture as well as information about its cooktime, ingredients, cuisine, diet, and allergens!", bg="light gray")
other_stuff.pack(pady=5)

more_instructions = tk.Label(subheading, text="↙ You can also filter for specific cook times and cuisines!", bg="light gray")
more_instructions.pack(pady=5)

#Side Filters
filters = tk.Frame(mainframe, bg="gray", width=200)
filters.pack(side="left", padx=10, pady=10, fill="y")

filters_canvas = tk.Canvas(filters,bg="gray", width=200,highlightbackground='grey')
filters_canvas.pack(side="left", padx=10, pady=10, fill="y")

filter_scroll = ttk.Scrollbar(filters, orient="vertical",takefocus= True, command=filters_canvas.yview)
filter_scroll.pack(side="right", fill="y")

filters_canvas.configure(yscrollcommand=filter_scroll.set)

frame_inside_canvas = tk.Frame(filters_canvas, bg="gray")
filters_canvas.create_window((0, 0), window=frame_inside_canvas, anchor="nw")

cooktime = tk.Frame(frame_inside_canvas, bg="gray")
cooktime.pack()

cooktime_title = tk.Label(frame_inside_canvas, text="Cook Time (in minutes)", bg="gray", fg="white",font=('Helvetica',15,'underline'))
cooktime_title.pack()

cooktimes = ["<60", ">=60 & <=120", ">120"]
for time in cooktimes:
    cooktime_filter = tk.Checkbutton(frame_inside_canvas, text=time, bg="gray")
    cooktime_filter.pack(anchor="w")

cuisines = tk.Frame(frame_inside_canvas, bg="gray")
cuisines.pack(padx=10, pady=10)

cuisines_label = tk.Label(frame_inside_canvas, text="Cuisines", bg="gray", fg="white",font=('Helvetica',15,'underline'))
cuisines_label.pack(anchor='w')

cuisine_list = ["African", "Asian", "American", "British", "Cajun", "Caribbean", "Chinese",
                "Eastern European", "European", "French", "German", "Greek", "Indian", "Irish", "Italian",
                "Japanese", "Jewish", "Korean", "Latin American", "Mediterranean", "Mexican",
                "Middle Eastern", "Nordic", "Southern", "Spanish", "Thai", "Vietnamese"]

for i in cuisine_list:
    cuisine = tk.Checkbutton(frame_inside_canvas, text=i, bg="gray")
    cuisine.pack(anchor="w")

def on_frame_configure(event):
    filters_canvas.configure(scrollregion=filters_canvas.bbox("all"))

frame_inside_canvas.bind("<Configure>", on_frame_configure)

#Recipe Frame
recipes = tk.Frame(mainframe, bg="white")
recipes.pack(fill="both", expand=True, padx=10, pady=10)

recipe_heading = tk.Label(recipes, text="Recipes", font=("Arial", 20, "bold"), bg="white")
recipe_heading.pack()

recipes_canvas = tk.Canvas(recipes, bg="white", highlightbackground='white')
recipes_canvas.pack(side="left", fill="both", expand=True)

recipes_scroll = ttk.Scrollbar(recipes, orient="vertical", command=recipes_canvas.yview)
recipes_scroll.pack(side="right", fill="y")

recipes_canvas.configure(yscrollcommand=recipes_scroll.set)

recipes_inner_frame = tk.Frame(recipes_canvas, bg="white")
recipes_canvas.create_window((0, 0), window=recipes_inner_frame, anchor="nw")

def on_recipes_configure(event):
    recipes_canvas.configure(scrollregion=recipes_canvas.bbox("all"))

recipes_inner_frame.bind("<Configure>", on_recipes_configure)

root.mainloop()

#sources:
# https://stackoverflow.com/questions/71677889/create-a-scrollbar-to-a-full-window-tkinter-in-python - used this to figure out how to scrol
# https://stackoverflow.com/questions/60594244/tkinter-scrollregion-not-updating?utm_source=chatgpt.com - updates the scroll region if its needed or not based on window size3

