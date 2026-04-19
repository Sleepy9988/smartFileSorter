from createFileDict import createFileList
from fileHash import createHash
from groupFiles import groupFiles

def iterateFileTree(pathObj, r, h):
    if not pathObj.exists():
        return
    try:
        for file in pathObj.iterdir():
            if file.is_file():
                file_hash = None
                if h:
                    try:
                        file_hash = createHash(file)
                    except Exception:
                        file_hash = "HASH_FAILED"

                yield from createFileList(file, file_hash)
            elif file.is_dir():
                yield from createFileList(file, None)

                if r:
                    yield from iterateFileTree(file, r, h)
    except PermissionError:
        return


def findEmptyDirs(pathObj, r):
    emptyDir = []
    is_empty = True
    if not pathObj.exists():
        return []
    try:
        for el in pathObj.iterdir():
            if el.is_file():
                is_empty = False
            elif el.is_dir() and r:
                result_empties = findEmptyDirs(el, r)
                emptyDir.extend(result_empties)
                if el not in result_empties:
                    is_empty = False
            elif el.is_dir() and not r:
                is_empty = False
        if is_empty:
            emptyDir.append(pathObj)
    except PermissionError:
        return []
    return emptyDir


def createFileTreeString(pathObj, r):
    files = list(iterateFileTree(pathObj, r, False))
    grouped_files = groupFiles(files)
    root_indent = getIndentLevel(pathObj)

    return_str = "File Tree:\n\n"
    for k,v in grouped_files.items():
        indent = (getIndentLevel(k) - root_indent) * "--"
        return_str += f"{indent}{k}\n"
        for el in v:
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


def getIndentLevel(pathObj):
    return len(pathObj.parts)