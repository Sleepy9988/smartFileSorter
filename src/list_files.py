
def list_files(path):
    for file in path.iterdir():
        if file.is_dir():
            list_files(file)
        print(file)