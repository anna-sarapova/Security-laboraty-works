import json
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser

root = Tk()
root.title('Auto Search Tool')
root.geometry("500x300")

# Update the listbox
def update(data):
    # Clear the listbox
    my_list.delete(0, END)

    # Add listing to listbox
    for item in data:
        my_list.insert(END, item)

# Update entry box with listbox clicked
def fillout(event):
    # Delere whatever is in the entry box
    my_entry.delete(0, END)

    # Add clinked list item to entry box
    my_entry.insert(0, my_list.get(ANCHOR))

# Create a function to check entry vs listbox
def check(e):
    # Grab what was typed
    typed = my_entry.get()

    if typed == '':
        data = listing
    else:
        data = []
        for item in listing:
            if typed.lower() in item.lower():
                data.append(item)
    
    # Update listbox with selected items
    update(data)

# Create a label
my_lable = Label(root, text="Start Typing...", font=("Helvetica", 14), fg="grey")
my_lable.pack(pady=20)

# Create an entry box
my_entry = Entry(root, font=("Helvetica", 20))
my_entry.pack()

# Create a listbox
my_list = Listbox(root, width=50)
my_list.pack(pady=40)

# Create a list for search bar
listing = ["password", "type", "description", "check_type", "group_policy", "name (stays for display_name)"]

# Add the searching items to the list
update(listing)

# Create a binding on the listbox onclick
my_list.bind("<<ListboxSelect>>", fillout)

# Create a binding on the entry box
my_entry.bind("<KeyRelease>", check)

root.mainloop()