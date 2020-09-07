import os

#storing path
path = '/Users/aakarsh.rajagopalan/Personal documents/Python projects/Renaming-files-automation/src-dir/'
#listing out the files in the src directory
list = os.listdir(path)

#declaring a variable to store count
i = 0
j = 1
#renaming the files in the directory
for file_name in enumerate(list):
    dst = "Wedding_photo_" + str(j) + ".jpg"
    print(file_name[i+1])
    src = path + file_name[i+1]

    #rename() will rename all files
    os.rename(src, dst)

    #incrementing counter
    j += 1



