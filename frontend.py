"""
A program that stores the book information
Title, Author, Year, ISBN

User can:

View all Records,
Search an Entry,
Add Entry,
Update Entry,
Delete Entry,
Close

"""


from tkinter import *
import backend 

def get_selected_row(event):
    try:
        global selected_tuple   # we can directly access this variable everywhere, and so no nee to return it
        index = list1.curselection()[0]  # To get the current selection list row index
        selected_tuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])

    except IndexError:
        pass

    

def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row) 

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)

def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.insert(END,(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_comment():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    
    

window = Tk()
window.wm_title("My Book Store")

l1 = Label(window, text = "Title")
l1.grid(row = 0, column = 0)

l2 = Label(window, text = "Author")
l2.grid(row = 0, column = 2)

l3 = Label(window, text = "Year")
l3.grid(row = 1, column = 0)

l4 = Label(window, text = "ISBN")
l4.grid(row = 1, column = 2)

title_text = StringVar()
e1 = Entry(window,textvariable=title_text)  # To accept the user input
e1.grid(row = 0, column = 1)

author_text = StringVar()
e2 = Entry(window,textvariable=author_text)  # To accept the user input
e2.grid(row = 0, column = 3)

year_text = StringVar()
e3 = Entry(window,textvariable=year_text)  # To accept the user input
e3.grid(row = 1, column = 1)

isbn_text = StringVar()
e4 = Entry(window,textvariable=isbn_text)  # To accept the user input
e4.grid(row = 1, column = 3)

list1 = Listbox(window, height=6,width=22)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

list1.bind('<<ListboxSelect>>', get_selected_row)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12, command= add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12, command=delete_comment)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()