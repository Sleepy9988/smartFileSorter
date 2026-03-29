def show_commands(cli_flags):
    command_str = "The available commands are:\n\n"
    for k, v in cli_flags.items():
        command_str += f"{k}: {v[2]}\n"

    command_str += "\nCommands -l, -b, -d, and -t can be run recursively to cover any existing child folders by adding the -r flag.\nWith flag -e the result can be extracted to a text file."
    return command_str