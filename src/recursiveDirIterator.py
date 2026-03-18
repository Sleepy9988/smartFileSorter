from createFileDict import createFileDict
from fileHash import createHash

def collectFiles(pathObj, r):
    fileList = []
    emptyDir = []
    is_empty = True
    if not pathObj:
        return ([], [])
    for file in pathObj.iterdir():
        is_empty = False
        if file.is_file():
            hash = createHash(file)
            fileList.extend(createFileDict(file, hash))
        if file.is_dir() and r:
            result_files, result_empties = collectFiles(file, r)
            fileList.extend(result_files)
            emptyDir.extend(result_empties)
    if is_empty == True:
        emptyDir.append(pathObj)
    return (fileList, emptyDir)