from dataclasses import dataclass

@dataclass
class Todo:
    """Represents a single task in the system."""
    id: int
    text: str
    is_completed: bool = False
