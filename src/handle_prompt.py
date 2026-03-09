import sys 
from pathlib import Path
from get_help import get_help
from list_files import list_files

cli_flags = {
    "-o": (True, "function placeholder"),
    "-h": (False, get_help),
    "-a": (True, get_help),
    "-m": (False, "function placeholder"),
    "-l": (True, list_files),
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
        path_obj = Path(path)

        if not path_obj.exists():
            raise ValueError("The provided path does not exist. Please provide a valid path.")
    
    if cli_flags[flag][0] == False and len(prompt_args) > 2:
        raise ValueError(f"{flag} takes only one argument.")

    cli_flags[flag][1](path_obj)