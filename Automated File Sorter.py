'''In this automatic file sorting script, I used the os module in python which allows you to use CLI features'''

# import os, and shutil module
import os, shutil

# read the path of the folder we will be sorting
path = r"C:/Users/White/Desktop/Python/python tutorials/"

# checking the contents in the folder
file_name = os.listdir(path)

# check if folder exists and create a folder if it doesn't 
folder_names = ['csv files', 'image files', 'pdf files']

for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
       # print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])

# check if file is not in folder
for file in file_name:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".png" in file and not os.path.exists(path + "png files" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".pdf" in file and not os.path.exists(path + "png files" + file):
        shutil.move(path + file, path + "pdf files/" + file)