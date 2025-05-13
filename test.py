import tkinter as tk
import webbrowser

root = tk.Tk()
root.geometry("750x250")

#Define a callback function
def callback(url):
    webbrowser.open_new_tab(url)

#Create a Label to display the link
link = tk.Label(root, text="www.google.com",
             font=('Helveticabold', 15), fg="blue", 
             cursor="hand2")
link.pack()
link.bind("<Button-1>", lambda e:
callback("http://www.google.com"))

root.mainloop()
