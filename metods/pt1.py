import os

path = input("Path: ")
term = input('Term: ')

for raiz, directories, files in os.walk(path):
    for file in files:
        if term in file:
            path_complete = os.path.join(raiz, file)
            name_archive, ext_file = os.path.splitext(file)

            print('File: ', file)
            print('Path: ', path_complete)
            print('Name: ', name_archive)
