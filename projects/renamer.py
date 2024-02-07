# Move and rename all .png files on your Desktop

# Identify all screenshots on your Desktop

# Create a new directory

# Move and rename all screenshots

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
