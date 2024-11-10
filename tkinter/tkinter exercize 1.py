import tkinter as tk
from tkinter.ttk import *


def greetings():
    print('hello!')

def open_file():
    with open('test_text/test', 'r') as saved_file:
        content = saved_file.read()
        print(content)

# Main window
main_window = tk.Tk()
main_window.title('Main Menu')
main_window.geometry('600x400')


# Menu
main_menu = tk.Menu(master = main_window)

# Add menu
main_window.config(menu = main_menu)


# File menu
file_menu = tk.Menu(master = main_window,
                    tearoff = False)

file_menu.add_command(label = 'Open',
                      command = open_file)

file_menu.add_separator()

main_menu.add_cascade(label = 'File',
                      menu = file_menu)


# Label
main_label = tk.Label(master = main_window,
                      text = 'main menu test')

main_label.pack()


# Button
hello_button = tk.Button(master = main_window,
                         text = 'Say hello!',
                         command = greetings)

hello_button.pack()


# Run
main_window.mainloop()
