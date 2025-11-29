from dataclasses import dataclass

from commands.command import Command


@dataclass
class ListCommand(Command):
    id: str = "list"

    def perform_action(self, args: list[str]) -> None:
        from config import PROJECTS

        print("===== Available Projects =====")
        for project in PROJECTS:
            print(project.id)

    def get_usage_message(self) -> str:
        return "Usage: list"
