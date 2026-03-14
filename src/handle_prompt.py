import sys 
from get_help import get_help
from list_files import printFiles, validatePath

cli_flags = {
    "-o": (True, "function placeholder"),
    "-h": (False, get_help),
    "-a": (True, get_help),
    "-m": (False, "function placeholder"),
    "-l": (True, printFiles),
}

def handle_user_prompt():
    prompt_args = sys.argv

    if len(prompt_args) < 2:
        raise ValueError("Missing arguments. Try again.")
    flag = prompt_args[1]
    
    if flag not in cli_flags:
        raise ValueError("Unknown argument. Operation cancelled.")
    
    if cli_flags[flag][0] == True:
        if not len(prompt_args) == 3:
            raise ValueError("Missing directory path.")
    
        path = prompt_args[2]
        pathObj = validatePath(path)
        if pathObj == None:
            raise ValueError("The provided path does not exist. Please provide a valid path.")
    
    if cli_flags[flag][0] == False and len(prompt_args) > 2:
        raise ValueError(f"{flag} takes only one argument.")

    cli_flags[flag][1](pathObj)