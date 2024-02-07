# Write a script that searches a folder you specify (as well as its subfolders, up
# to two levels deep) and compiles a list of all `.jpg` files contained in there.
# The list should include the complete path of each `.jpg` file.
# 
# You should train:
# 
# - Using `for` loops
# - Using conditional statements
# - Working with `pathlib`
# - Thinking about nested loops
# 
# If you are feeling bold, create a list containing each type of file extension
# you find in the folder.
# Start with a small folder to make it easy to check whether your program is
# working correctly. Then search a bigger folder.
# This program should work for any specified folder on your computer.

import pathlib

scrennshots = pathlib.Path(r"C:\Users\simon\OneDrive\Desktop\screeshots")

for index, filepath in enumerate(scrennshots.iterdir()):
    if filepath.suffix == ".jpg" or filepath.suffix == ".png":
        # create new path
        scrennshot = pathlib.Path(r"C:\Users\simon\OneDrive\Desktop\screeshots")
        scrennshot = scrennshot.joinpath(str(index) + "_" + filepath.name)
        print("Print result:", scrennshot)
        # Move the File
        filepath.replace(scrennshot)
