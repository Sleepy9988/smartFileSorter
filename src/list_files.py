from pathlib import Path

def validatePath(path):
    path_obj = Path(path)
    if path_obj.exists():
        return path_obj
    return None

def collectFiles(pathObj):
    fileList = []
    if not pathObj:
        return []
    for file in pathObj.iterdir():
        fileList.extend(createFileDict(file))
        if file.is_dir():
            fileList += collectFiles(file)
    return fileList

def createFileDict(pathObj):
    fileDict = {
        "parent_dir": pathObj.parent,
        "isFile": pathObj.is_file(),
        "extension": pathObj.suffix,
        "name": pathObj.stem,
        "fullname": pathObj.name,
    }
    return [fileDict]


def printFiles(pathObj):
    files = collectFiles(pathObj)
    print(f"Parent: {files[0]["parent_dir"]}")
    for i in range(len(files)):
        j = 1
        if files[j]["parent_dir"] != files[i]["parent_dir"]:
            print(f"{files[i]["parent_dir"]}")
        j += 1
        if files[i]["isFile"]:
            print(f"\tFile {i + 1}: {files[i]["fullname"]}")

        #print(file["parent_dir"])

"""
class File:
    def __init__(self, path):
        self.pathObj = Path(path)
        self.parent_dir = self.pathObj.parent
        self.isFile = self.pathObj.is_file()
        self.ext = self.pathObj.suffix
        self.name = self.pathObj.stem

    def __repr__(self):
        if self.isFile:
            return f"File: {self.name}{self.ext}"
        return f"Folder: {self.name}"
"""       