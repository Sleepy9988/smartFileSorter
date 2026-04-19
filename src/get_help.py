
def get_help(cli_flags):
    """
    Generates a detailed help manual based on the available CLI flags.
    """
    help_str = "--- Smart File Sorter Help ---\n"
    help_str += "Usage: python main.py [COMMAND] [PATH] [FLAGS]\n\n"
    help_str += "Available Commands:\n"
    
    # Iterate through the dictionary you defined in cli_flags.py
    for flag, info in cli_flags.items():
        requires_path = " [path]" if info[0] else ""
        description = info[2]
        help_str += f"  {flag}{requires_path:10} : {description}\n"

    help_str += "\nOptional Flags:\n"
    help_str += "  -r           : Recursive mode (include all subdirectories).\n"
    help_str += "  -e           : Export results to a .txt file.\n"
    
    help_str += "\nExample:\n"
    help_str += "  python main.py -t ./my_folder -r -e\n"
    help_str += "  (Show tree of 'my_folder' recursively and export to text)\n"
    
    return help_str