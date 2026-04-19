from pathlib import Path
from recursiveDirIterator import iterateFileTree
import json 

def load_config():
    config_path = Path(__name__).parent / "config.json"
    with open(config_path, "r") as f:
        return json.load(f)


def parseDirectory(pathObj, r):
    file_ext_map = load_config()
    files = iterateFileTree(pathObj, r, False)
    counter = 0
    for file in files:
        if file["isFile"] == True:
            for k,v in file_ext_map.items():
                if file["extension"] in v:
                    dest = k
                    counter += moveFiles(Path(file["parent_dir"] / file["fullname"]), Path(pathObj / dest))

    return f"{counter} files moved"
       
    

def moveFiles(src_file, dest_loc):
    dest_loc.mkdir(parents=True, exist_ok=True)
    src_file.replace(dest_loc / src_file.name)
    return 1