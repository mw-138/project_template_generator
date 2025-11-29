from dataclasses import dataclass, field
from typing import Self


@dataclass
class StringBuilder:
    _string: list[str] = field(default_factory=list)

    def add(self, text: str) -> Self:
        self._string.append(text)
        return self

    def get(self) -> str:
        return "\n".join(self._string)
