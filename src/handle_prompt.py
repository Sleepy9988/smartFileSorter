import sys 
from get_help import get_help
from validatePath import validatePath
from recursiveDirIterator import createFileTreeString, createEmptyDirString
from runAnalyses import runAnalyses
from compareHashValues import findDupHashValues

cli_flags = {
    "-l": (True, runAnalyses),
    "-h": (False, get_help),
    "-b": (True, createEmptyDirString),
    "-d": (True, findDupHashValues),
    "-e": (False, "function placeholder"),
    "-t": (True, createFileTreeString),
    "-o": (False, "function placeholder"),
    "-m": (False, "function placeholder"),
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

    result = cli_flags[flag][1](pathObj, True)
    print(result)