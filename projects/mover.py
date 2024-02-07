# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib

# Find the path to my Desktop

# Create a new folder

# Filter for screenshots only

# Create a new path for each file

# Move the screenshot there

import pathlib

home = pathlib.Path(r"C:\Users\simon\OneDrive\Desktop")
scrennshot = pathlib.Path(r"C:\Users\simon\OneDrive\Desktop\screeshots")
if scrennshot.exists() == False:
    scrennshot.mkdir()

for filepath in home.iterdir():
    if filepath.suffix == ".jpg" or filepath.suffix == ".png":
        # create new path
        scrennshot = pathlib.Path(r"C:\Users\simon\OneDrive\Desktop\screeshots")
        scrennshot = scrennshot.joinpath(filepath.name)
        print("Print result:", scrennshot)
        # Move the File
        filepath.replace(scrennshot)
