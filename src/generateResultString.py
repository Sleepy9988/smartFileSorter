from runAnalyses import runAnalyses
from groupFiles import groupFiles
from recursiveDirIterator import collectFiles

def printFiles(pathObj, r):
    (files, emptyDirs) = collectFiles(pathObj, r)
    print(files)
    grouped_files = groupFiles(files)
   
    root_indent = getIndentLevel(files[0]["parent_dir"])

    print(runAnalyses(files))
    for el in emptyDirs:
        print(f"Empty directories:\n {el}\n")
    for k,v in grouped_files.items():
        indent = (getIndentLevel(k) - root_indent) * "--"
        print("File Tree:")
        print(f"{indent}{k}")
        for el in v:
            if el["isFile"]:
                print(f'{indent + "--"}{el["fullname"]}')


def getIndentLevel(path):
    parent_parts = str(path).split("/")
    return len(parent_parts)
