from organizeDir import load_config

def showOrgaDirs(*args):
    file_ext_map = load_config()
    return_str = "Folder name - File types\n\n"
    for k, v in file_ext_map.items():
        return_str += f"{k} - {v}\n"
    return return_str