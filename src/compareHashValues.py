from recursiveDirIterator import iterateFileTree

def findDupHashValues(files):
    hash_dict = {}
    for file in files:
        if file["hash"] not in hash_dict:
            hash_dict[file["hash"]] = 0
        hash_dict[file["hash"]] += 1
    
    duplicate_dict = {key: val for key, val in hash_dict.items() if val > 1}
    return duplicate_dict

def createDuplicateString(pathObj, r):
    files = iterateFileTree(pathObj, r)
    duplicates = findDupHashValues(files)

    total = 0
    for k, v in duplicates.items():
        total += v
   
    return_str = f"There are {total} files with identical content.\n"
    for file in files:
        if file["hash"] in duplicates:
            return_str += f"{file["fullname"]} - {file["hash"]}\n"
    return return_str




