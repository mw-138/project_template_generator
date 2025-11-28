from dataclasses import dataclass

from projects.project import Project


@dataclass
class ProjectGenerator:
    def generate(self, project: Project) -> None:
        pass
