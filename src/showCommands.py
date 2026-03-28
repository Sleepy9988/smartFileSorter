def show_commands(cli_flags):
    command_str = "The available commands are:\n\n"
    for k, v in cli_flags.items():
        command_str += f"{k}: {v[2]}\n"
    return command_str