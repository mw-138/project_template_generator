from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class ProjectFile:
    name: str
    text: str


@dataclass
class ProjectDirectory:
    path: str
    files: list[ProjectFile]


@dataclass
class Project:
    id: str
    name: str = ""
    directories: list[ProjectDirectory] = field(default_factory=list)

    def generate(self, path: str, project_name: str) -> None:
        self.name = project_name
        root_path = f"{path}/{project_name}"
        project_dir = Path(root_path)

        try:
            project_dir.mkdir()
        except Exception:
            print("Project already exists")
            return

        for dir in self.directories:
            dir_path = Path(f"{root_path}/{dir.path}")
            (project_dir / dir.path).mkdir(parents=True, exist_ok=True)
            for file in dir.files:
                (dir_path / file.name).write_text(file.text)
