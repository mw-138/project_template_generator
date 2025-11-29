from commands.command import Command
from commands.create_command import CreateCommand
from commands.help_command import HelpCommand
from commands.list_command import ListCommand
from projects.lua_project import LuaProject
from projects.project import Project
from projects.python_project import PythonProject
from projects.typescript_project import TypescriptProject

COMMANDS: list[Command] = [CreateCommand(), ListCommand(), HelpCommand()]
PROJECTS: list[Project] = [PythonProject(), LuaProject(), TypescriptProject()]
