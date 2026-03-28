import os
import uuid

def exportToTxt(text, path):
    filename = f"smartFileSorter_extract_ {uuid.uuid1()}.txt"

    with open(os.path.join(path,filename), "w", encoding="utf-8") as f:
        f.write(text)
    print()