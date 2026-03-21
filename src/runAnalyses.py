from recursiveDirIterator import iterateFileTree

def runAnalyses(pathObj, r):
    files = iterateFileTree(pathObj, r)
    num_files = 0
    num_dirs = 0
    extension_dict = {}
    for file in files:
        if file["isFile"]:
            num_files += 1
            if file["extension"] not in extension_dict:
                extension_dict[file["extension"]] = 0
            extension_dict[file["extension"]] += 1
        else:
            num_dirs += 1
    return_str = f"There are {num_files} files and {num_dirs} directories in path {pathObj}\n\nFile types:\n"
    for k,v in extension_dict.items():
        return_str += f"{k}:\t {v}\n"
    return return_str
        