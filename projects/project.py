from dataclasses import dataclass


@dataclass
class Project:
    id: str
    directories: list[str]

    def generate(self) -> None:
        pass
