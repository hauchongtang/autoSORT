import os
import shutil
import time

path = "D:/Sorter"

file_list = os.listdir(path)
# sort and create new folder with extension name
def sort_extension():
    for file in file_list:
        name, extension = os.path.splitext(file)

        # Store file extension
        extension = extension[1:]

        # Detect if a folder is inside path then continue iteration
        if extension == '':
            continue

        if os.path.exists(path + "/" + extension):
            shutil.move(path + "/" + file, "/" + extension + "/" + file)
        else:
            os.makedirs(path + "/" + extension)
            shutil.move(path + "/" + file, path + "/" + extension + "/" + file)

# after folders are created, sort according to alphabatical order
def sort_alphabetical():
    for file in file_list:
        name = os.path.splitext(file)
        sorted_name = sorted(name)

# Function to run both one after another --> sort by extension then by alphabetical order
def sort_():
    sort_extension()
    sort_alphabetical()

# Prevents endless looping
while True:
   sort_()
   time.sleep(10)



