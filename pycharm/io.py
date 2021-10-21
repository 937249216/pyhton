import os


def getAllFiles(path, level):
    childfiles = os.listdir(path)
    for file in childfiles:
        filepath = os.path.join(path, file)
        if os.path.isdir(filepath):
            getAllFiles(filepath, filepath)
        print("\t" * level + filepath)


getAllFiles("../learn", 0)
