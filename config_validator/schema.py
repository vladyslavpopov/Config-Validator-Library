from typing import Any, Dict

class Schema:
    def __init__(self):
        self.fields: Dict[str, Dict[str, Any]] = {}

    def add_field(self, name: str, field_type: type, required: bool = True) -> None:
        self.fields[name] = {"type": field_type, "required": required}