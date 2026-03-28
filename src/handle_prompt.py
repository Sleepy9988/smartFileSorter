import sys 
from validatePath import validatePath
from export import exportToTxt
from cli_flags import cli_flags

def handle_user_prompt():
    prompt_args = sys.argv[1:]
    export = False
    recursive = False
    path_required = False
    command_flag = None

    if not prompt_args:
        raise ValueError("You did not provide any command. Please provide a command and try again.")

    if "-r" in prompt_args:
        recursive = True
        prompt_args.remove("-r")
    if "-e" in prompt_args:
        export = True
        prompt_args.remove("-e")
    
    for flag in cli_flags:
        if flag in prompt_args:
            command_flag = flag
            prompt_args.remove(command_flag)
            break
    if command_flag is None:
        raise ValueError("Unknown argument. Operation cancelled.")
    
    if cli_flags[command_flag][0]:
        path_required = True
    
    if cli_flags[command_flag][0] == True:
        if not prompt_args:
            raise ValueError("Missing path")
        path = prompt_args[0]
        pathObj = validatePath(path)
        if pathObj == None:
            raise ValueError("The provided path does not exist. Please provide a valid path.")

    if path_required:
        result = cli_flags[command_flag][1](pathObj, recursive)
    else:
        result = cli_flags[command_flag][1](cli_flags)
    print(result)

    if export:
        output_path = input("Provide a path to export to\n")
        export_to = validatePath(output_path)
        if not export_to:
            export_to = "/tmp"
        exportToTxt(result, export_to)



        