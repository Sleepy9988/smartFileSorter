from get_help import get_help
from recursiveDirIterator import createFileTreeString, createEmptyDirString
from runAnalyses import runAnalyses
from compareHashValues import createDuplicateString
from organizeDir import parseDirectory
from showCommands import show_commands

cli_flags = {
    "-l": (True, runAnalyses, "Count the files and folders in the given directory."),
    "-h": (False, get_help, "Provide help on the specified command."),
    "-b": (True, createEmptyDirString, "Search for empty sub-directories in the given directory."),
    "-d": (True, createDuplicateString, "Find identical files in the given directory."),
    "-t": (True, createFileTreeString, "Show the file tree of the given directory."),
    "-o": (True, parseDirectory, "Organize the files in the given directory into subfolders based on their extension."),
    "-m": (False, "function placeholder", ""),
    "-c": (False, show_commands, "List the available commands."),

}