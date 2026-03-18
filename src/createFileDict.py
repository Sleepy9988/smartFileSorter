def createFileDict(pathObj, hash):
    fileDict = {
        "parent_dir": pathObj.parent,
        "isFile": pathObj.is_file(),
        "extension": pathObj.suffix or "binary",
        "name": pathObj.stem,
        "fullname": pathObj.name,
        "hash": hash
    }
    return [fileDict]