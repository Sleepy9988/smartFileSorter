from pathlib import Path
from recursiveDirIterator import iterateFileTree

file_ext_map = {
    "Documents": [".docx", ".doc", ".txt", ".pdf", ".md"],
    "Spreadsheet": [".xls", ".xlsx", ".csv"],
    "Executables": [".exe"],
    "Zip": [".zip", ".rar"],
    "Images": [".jpeg", ".png", ".jpg", ".svg"],
    "Presentations": [".pptx", ".ppt"],
    "Video": [".mp4"],
    "Audio": [".wav", ".mp3", ".aac"]
}

def parseDirectory(pathObj, r):
    files = iterateFileTree(pathObj, False)
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