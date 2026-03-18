def groupFiles(files):
    ordered_file_dict = {}
    for file in files: 
        if file["parent_dir"] not in ordered_file_dict:
            ordered_file_dict[file["parent_dir"]] = []
        ordered_file_dict[file["parent_dir"]].append(file)
    return ordered_file_dict