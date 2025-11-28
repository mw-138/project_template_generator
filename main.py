import sys

from config import COMMANDS


def main():
    args = sys.argv
    arg_len = len(args)

    if arg_len < 2:
        print("No command provided")
        return

    command = args[1].lower()
    found_command = next((c for c in COMMANDS if c.id == command), None)
    if found_command:
        found_command.perform_action(args[2:])
    else:
        print("command not found")


if __name__ == "__main__":
    main()
