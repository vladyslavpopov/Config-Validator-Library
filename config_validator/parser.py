import json
import yaml
import toml
from pathlib import Path
from .exceptions import InvalidFileFormatError

def parse_config(file_path: str) -> dict:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if path.suffix == ".json":
        with open(path, "r") as f:
            return json.load(f)
    elif path.suffix in (".yaml", ".yml"):
        with open(path, "r") as f:
            return yaml.safe_load(f)
    elif path.suffix == ".toml":
        with open(path, "r") as f:
            return toml.load(f)
    else:
        raise InvalidFileFormatError("Unsupported file format. Use JSON, YAML, or TOML.")