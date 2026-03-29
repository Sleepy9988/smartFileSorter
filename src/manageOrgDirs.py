from organizeDir import file_ext_map

def showOrgaDirs(*args):
    return_str = "Folder name - File types\n\n"
    for k, v in file_ext_map.items():
        return_str += f"{k} - {v}\n"
    return return_str