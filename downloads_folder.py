import os
import shutil

# Write the name of the directory here, that needs to get sorted
path = 'enter your path here'

# List with all the filename that are in the directory
list_ = os.listdir(path)

# This will go through each and every file
for file_ in list_:
    # This checks if 'file_' is indeed a file
    if os.path.isfile(path + '/' + file_):
        name, ext = os.path.splitext(file_)
    else:
        continue

    # Extension type
    ext = ext[1:]

    # File to the directory of the name 'ext' if already exists
    if os.path.exists(path + '/' + ext):
        shutil.move(path + '/' + file_, path + '/' + ext + '/' + file_)

    # Creates a new directory, if the directory does not already exist
    else:
        os.makedirs(path + '/' + ext)
        shutil.move(path + '/' + file_, path + '/' + ext + '/' + file_)
