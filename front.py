from tkinter import *
import backend

def add_():
    #Button for Adding Entry
    backend.add(title_text.get(),
                    author_text.get(),
                    year_text.get(), 
                    isbn_text.get())
    listing.delete(0, END)
    listing.insert(END, 
                    (title_text.get(), 
                    author_text.get(), 
                    year_text.get(), 
                    isbn_text.get()))

def view_():
    #Button for Viewing Entries
    listing.delete(0, END)
    for row in backend.seek():
        listing.insert(END, row)

def update_():
    #Button for Updating Entries
    backend.modify(selected_tuple[0], 
                    title_text.get(), 
                    author_text.get(), 
                    year_text.get(), 
                    isbn_text.get())

def delete_():
    #Button for Deleting Entry
    backend.delete(selected_tuple[0])

def search_():
    #Button for Search
    listing.delete(0, END)
    for row in backend.search(title_text.get(), 
                                author_text.get(), 
                                year_text.get(), 
                                isbn_text.get()):
        listing.insert(END, row)

def get_selected_row(event):
    """Pre-fill fields for selected entry."""
    global selected_tuple
    index = listing.curselection()[0]
    selected_tuple = listing.get(index)

    entry1.delete(0, END)
    entry1.insert(END, selected_tuple[1])

    entry2.delete(0, END)
    entry2.insert(END, selected_tuple[2])

    entry3.delete(0, END)
    entry3.insert(END, selected_tuple[3])

    entry4.delete(0, END)
    entry4.insert(END, selected_tuple[4])

window = Tk()
window.geometry("600x200")
window.wm_title("Book Directory")
window.configure(background = "powder blue")

exit_icon = PhotoImage(file='C:/Users/Raven/Desktop/exit.png')
view_icon = PhotoImage(file='C:/Users/Raven/Desktop/view.png')
select_icon = PhotoImage(file='C:/Users/Raven/Desktop/select.png')
delete_icon = PhotoImage(file='C:/Users/Raven/Desktop/delete.png')
search_icon = PhotoImage(file='C:/Users/Raven/Desktop/search.png')
add_icon = PhotoImage(file='C:/Users/Raven/Desktop/add.png')

# Labels for entry fields.
label1 = Label(window, text = "Book Name", bg="powder blue")
label1.grid(row = 10, column = 0)

label2 = Label(window, text = "Writer", bg="powder blue")
label2.grid(row = 10, column = 5)

label3 = Label(window, text = "Year", bg="powder blue")
label3.grid(row = 11, column = 0)

label4 = Label(window, text = "ISBN No.", bg="powder blue")
label4.grid(row = 11, column = 5)

# Entry Fields.
title_text = StringVar()
entry1 = Entry(window, textvariable = title_text)
entry1.grid(row = 10, column = 1)
entry1.configure({"background":"white"})

author_text = StringVar()
entry2 = Entry(window, textvariable = author_text)
entry2.grid(row = 10, column = 3)
entry2.configure({"background":"white"})

year_text = StringVar()
entry3 = Entry(window, textvariable = year_text)
entry3.grid(row = 11, column = 1)
entry3.configure({"background":"white"})

isbn_text = StringVar()
entry4 = Entry(window, textvariable = isbn_text)
entry4.grid(row = 11, column = 3)
entry4.configure({"background":"white"})

# List all data.
listing = Listbox(window, height = 9, width = 50)
listing.grid(row = 0, column = 0, rowspan = 6, columnspan = 3)
listing.configure({"background":"light yellow"})

# Scrollbar.
scroller = Scrollbar(window)
scroller.grid(row = 0, column = 2, rowspan = 6)

# Configure scrollbar for Listbox.
listing.configure(yscrollcommand = scroller.set)
scroller.configure(command = listing.yview)

listing.bind('<<ListboxSelect>>', get_selected_row)

# Buttons for various operations on data.
button1 = Button(window, 
                text = "View", 
                width = 12, 
                command = view_,
                bg = "steel blue",
                image = view_icon)
button1.grid(row = 2, column = 8)

button2 = Button(window, 
                text = "Search", 
                width = 12, 
                command = search_,
                bg = "steel blue",
                image = search_icon)
button2.grid(row = 1, column = 8)

button3 = Button(window, 
                text = "Add Details", 
                width = 12, 
                command = add_,
                bg = "steel blue",
                image = add_icon)
button3.grid(row = 1, column = 5)

button4 = Button(window, 
                text = "Select & Update", 
                width = 12, 
                command = update_,
                bg = "steel blue",
                image = select_icon)
button4.grid(row = 2, column = 5)

button5 = Button(window, 
                text = "Select & Delete", 
                width = 12, 
                command = delete_,
                bg = "steel blue",
                image = delete_icon)
button5.grid(row = 3, column = 5)

button6 = Button(window, 
                text = "Exit", 
                width = 12, 
                command = window.destroy,
                bg = "red",
                relief = SUNKEN,
                image = exit_icon)
button6.grid(row = 3, column = 8)

label5 = Label(window, text = "Add", bg="powder blue")
label5.grid(row = 1, column = 4)

label6 = Label(window, text = "Search", bg="powder blue")
label6.grid(row = 1, column = 7)

label7 = Label(window, text = "Delete", bg="powder blue")
label7.grid(row = 3, column = 4)

label8 = Label(window, text = "Select", bg="powder blue")
label8.grid(row = 2, column = 4)

label9 = Label(window, text = "View", bg="powder blue")
label9.grid(row = 2, column = 7)

label10 = Label(window, text = "Exit", bg="powder blue")
label10.grid(row = 3, column = 7)

#Screen hold.
window.mainloop()
