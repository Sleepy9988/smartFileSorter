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
        