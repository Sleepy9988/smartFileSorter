from pathlib import Path

def validatePath(path):
    path_obj = Path(path)
    if path_obj.exists():
        return path_obj
    return None

def collectFiles(pathObj, r):
    fileList = []
    if not pathObj:
        return []
    for file in pathObj.iterdir():
        fileList.extend(createFileDict(file))
        if file.is_dir() and r:
            fileList += collectFiles(file, r)
    return fileList

def createFileDict(pathObj):
    fileDict = {
        "parent_dir": pathObj.parent,
        "isFile": pathObj.is_file(),
        "extension": pathObj.suffix or "binary",
        "name": pathObj.stem,
        "fullname": pathObj.name,
    }
    return [fileDict]


def getIndentLevel(path):
    parent_parts = str(path).split("/")
    return len(parent_parts)

def printFiles(pathObj, r):
    files = collectFiles(pathObj, r)
    
    grouped_files = groupFiles(files)
    root_indent = getIndentLevel(files[0]["parent_dir"])

    print(runAnalyses(files))
    for k,v in grouped_files.items():
        indent = (getIndentLevel(k) - root_indent) * "--"
        
        print(f"{indent}{k}")
        for el in v:
            if el["isFile"]:
                print(f'{indent + "--"}{el["fullname"]}')
   

def runAnalyses(files_list):
    num_files = 0
    num_dirs = 0
    extension_dict = {}
    for file in files_list:
        if file["isFile"]:
            num_files += 1
            if file["extension"] not in extension_dict:
                extension_dict[file["extension"]] = 0
            extension_dict[file["extension"]] += 1
        else:
            num_dirs += 1
    return_str = f"There are {num_files} files and {num_dirs} directories.\n"
    for k,v in extension_dict.items():
        return_str += f"{k}:\t {v}\n"
    return return_str
        

def groupFiles(files):
    ordered_file_dict = {}
    for file in files: 
        if file["parent_dir"] not in ordered_file_dict:
            ordered_file_dict[file["parent_dir"]] = []
        ordered_file_dict[file["parent_dir"]].append(file)
    return ordered_file_dict

