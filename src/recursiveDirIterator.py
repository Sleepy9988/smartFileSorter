from createFileDict import createFileList
from fileHash import createHash
from groupFiles import groupFiles

def iterateFileTree(pathObj, r):
    fileList = []
    if not pathObj:
        return []
    for file in pathObj.iterdir():
        if file.is_file():
            hash = createHash(file)
            fileList.extend(createFileList(file, hash))
        if file.is_dir() and r:
            result_files = iterateFileTree(file, r)
            fileList.extend(result_files)
    return fileList


def findEmptyDirs(pathObj, r):
    emptyDir = []
    is_empty = True
    if not pathObj:
        return []
    for el in pathObj.iterdir():
        is_empty = False
        if el.is_dir() and r:
            result_empties = findEmptyDirs(el, r)
            emptyDir.extend(result_empties)
    if is_empty == True:
        emptyDir.append(pathObj)
    return emptyDir


def createFileTreeString(pathObj, r):
    files = iterateFileTree(pathObj, r)
    grouped_files = groupFiles(files)
    root_indent = getIndentLevel(files[0]["parent_dir"])

    return_str = "File Tree:\n\n"
    for k,v in grouped_files.items():
        indent = (getIndentLevel(k) - root_indent) * "--"
        return_str += f"{indent}{k}\n"
        for el in v:
            if el["isFile"]:
                return_str += f'{indent + "--"}{el["fullname"]}\n'
    return return_str

def createEmptyDirString(pathObj, r):
    emptyDirs = findEmptyDirs(pathObj, r)
    dir_str = "directories"
    verb = "are"
    if len(emptyDirs) == 1:
        verb = "is"
        dir_str = "directory"
    return_str = f"There {verb} {len(emptyDirs)} empty {dir_str} in path {pathObj}\n\n"
    for el in emptyDirs:
        return_str += f"{el}\n"
    return return_str


def getIndentLevel(path):
    parent_parts = str(path).split("/")
    return len(parent_parts)