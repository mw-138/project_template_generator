from dataclasses import dataclass

from commands.command import Command


@dataclass
class CreateCommand(Command):
    def perform_action(self, args: list[str]) -> None:
        from config import PROJECTS

        if len(args) < 1:
            print(self.get_usage_message())
            return

        project_id = args[0]
        found_project = next(
            (project for project in PROJECTS if project.id == project_id), None
        )

        if not found_project:
            print(f"Project '{project_id}' is not a valid project type")
            return

        print(f"===== Creating project '{project_id}' =====")
        found_project.generate()

    def get_usage_message(self) -> str:
        return "Usage: create <project_type>"
