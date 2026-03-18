from pathlib import Path

def validatePath(path):
    path_obj = Path(path)
    if path_obj.exists():
        return path_obj
    return None








