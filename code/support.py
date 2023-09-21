import os
from os import walk




def import_folder(path):
    surface_list = []

    print(path)
    for root, dirs, files in walk(".\graphics\character", topdown=False):
        for name in files:
            print(name)
            print(os.path.join(root, name))
        # for name in dirs:
            # print(os.path.join(root, name))

    return surface_list