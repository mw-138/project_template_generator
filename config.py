from commands.command import Command
from commands.create_command import CreateCommand
from commands.help_command import HelpCommand
from commands.list_command import ListCommand
from projects.project import Project

COMMANDS: list[Command] = [
    CreateCommand("create"),
    ListCommand("list"),
    HelpCommand("help"),
]

PROJECTS: list[Project] = [Project("simple_python", ["main.py"])]
