from tkinter import *
import shutil
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb


def count_characters():
    # open file in read mode
    file = open("data.txt", "r")

    # read the content of file
    data = file.read()

    # get the length of the data
    number_of_characters = len(data)

    print('Number of characters in text file :', number_of_characters)
    # Major functions of file manager
    file.close()
    return number_of_characters


def count_without_space():
    # open file in read mode
    file = open("data.txt", "r")

    # read the content of file and replace spaces with nothing
    data = file.read().replace(" ", "")

    # get the length of the data
    number_of_characters = len(data)

    print('Number of characters in text file :', number_of_characters)
    return number_of_characters


def count_occurances():
    # get file object reference to the file
    file = open("data.txt", "r")

    # read content of file to string
    data = file.read()

    # get number of occurrences of the substring in the string
    occurrences = data.count("Quem")

    print('Number of occurrences of the word :', occurrences)
    return occurrences


# open a file box window
# when we want to select a file
def open_window():
    read = easygui.fileopenbox()
    return read


# open file function
def open_file():
    string = open_window()
    try:
        os.startfile(string)
    except FileNotFoundError:
        mb.showinfo('confirmation', "File not found!")


# copy file function
def copy_file():
    source1 = open_window()
    destination1 = filedialog.askdirectory()
    shutil.copy(source1, destination1)
    mb.showinfo('confirmation', "File Copied !")


# delete file function
def delete_file():
    del_file = open_window()
    if os.path.exists(del_file):
        os.remove(del_file)
    else:
        mb.showinfo('confirmation', "File not found !")


# rename file function
def rename_file():
    chosenfile = open_window()
    path1 = os.path.dirname(chosenfile)
    extension = os.path.splitext(chosenfile)[1]
    print("Enter new name for the chosen file")
    newname = input()
    path = os.path.join(path1, newname + extension)
    print(path)
    os.rename(chosenfile, path)
    mb.showinfo('confirmation', "File Renamed !")


# move file function
def move_file():
    source = open_window()
    destination = filedialog.askdirectory()
    if source == destination:
        mb.showinfo('confirmation', "Source and destination are same")
    else:
        shutil.move(source, destination)
        mb.showinfo('confirmation', "File Moved !")


# function to make a new folder
def make_folder():
    newfolderpath = filedialog.askdirectory()
    print("Enter name of new folder")
    newfolder = input()
    path = os.path.join(newfolderpath, newfolder)
    os.mkdir(path)
    mb.showinfo('confirmation', "Folder created !")


# function to remove a folder
def remove_folder():
    delfolder = filedialog.askdirectory()
    os.rmdir(delfolder)
    mb.showinfo('confirmation', "Folder Deleted !")


# function to list all the files in folder
def list_files():
    folderlist = filedialog.askdirectory()
    sortlist = sorted(os.listdir(folderlist))
    i = 0
    print("Files in ", folderlist, "folder are:")
    while i < len(sortlist):
        print(sortlist[i] + '\n')
        i += 1


# Creating the UI of our file manager

root = Tk()

# creating label and buttons to perform operations
Label(root, text="260756 File Manager System", font=("Helvetica", 16), fg="blue").grid(row=5, column=2)

Button(root, text="Count all characters in a text file", command=count_characters).grid(row=15, column=2)

Button(root, text="Count all characters without space", command=count_without_space).grid(row=25, column=2)

Button(root, text="Count occurances", command=count_occurances).grid(row=35, column=2)

Button(root, text="Open a File", command=open_file).grid(row=45, column=2)

Button(root, text="Copy a File", command=copy_file).grid(row=55, column=2)

Button(root, text="Delete a File", command=delete_file).grid(row=65, column=2)

Button(root, text="Rename a File", command=rename_file).grid(row=75, column=2)

Button(root, text="Move a File", command=move_file).grid(row=85, column=2)

Button(root, text="Make a Folder", command=make_folder).grid(row=95, column=2)

Button(root, text="Remove a Folder", command=remove_folder).grid(row=105, column=2)

Button(root, text="List all Files in Directory", command=list_files).grid(row=115, column=2)

root.mainloop()
