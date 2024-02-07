# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.
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



