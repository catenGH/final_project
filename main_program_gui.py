#Imports
from tkinter import ttk
import tkinter as tk
import requests
from PIL import ImageTk, Image
from io import BytesIO

#Function Imports
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

search = tk.Button(heading, text="🔎", highlightbackground='mediumorchid3')
search.pack(side="right", padx=20)

add_ingredient = tk.Button(heading, text="✚",highlightbackground='mediumorchid3')
add_ingredient.pack(side="right", padx=10)

ingredient = tk.StringVar()
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

recipes = tk.Frame(mainframe, bg="white")
recipes.pack(fill="both", padx=10, pady=10)

recipe_heading = tk.Label(recipes, text="Recipes", font=(20), bg="white")
recipe_heading.pack()

for i in range(0, 3):
    recipe_box = tk.Frame(recipes, bg="gray", bd=2, padx=10, pady=10)
    recipe_box.pack(side="left", padx=10, pady=10)
    recipe_title = tk.Label(recipe_box, text="example", bg="gray")
    recipe_title.pack(anchor="w")

def on_frame_configure(event):
    filters_canvas.configure(scrollregion=filters_canvas.bbox("all"))

filters_canvas.bind("<Configure>", on_frame_configure)

root.mainloop()

#sources:
# https://stackoverflow.com/questions/71677889/create-a-scrollbar-to-a-full-window-tkinter-in-python - used this to figure out how to scrol
# https://stackoverflow.com/questions/60594244/tkinter-scrollregion-not-updating?utm_source=chatgpt.com - updates the scroll region if its needed or not based on window size3

