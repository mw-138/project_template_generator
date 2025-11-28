from dataclasses import dataclass


@dataclass
class Command:
    id: str

    def perform_action(self, args: list[str]) -> None:
        pass

    def get_usage_message(self) -> str:
        return ""
