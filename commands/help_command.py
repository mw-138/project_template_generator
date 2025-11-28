from dataclasses import dataclass

from commands.command import Command


@dataclass
class HelpCommand(Command):
    def perform_action(self, args: list[str]) -> None:
        from config import COMMANDS

        print("===== Help =====")
        for command in COMMANDS:
            print(f"{command.id} - {command.get_usage_message()}")

    def get_usage_message(self) -> str:
        return "Usage: help"
