import json
import yaml
import toml
from pathlib import Path
from config_validator.exceptions import InvalidFileFormatError

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
        try:
            import toml
            with open(path, "r", encoding="utf-8") as f:
                return toml.load(f)
        except ImportError:
            raise ImportError("TOML support requires 'toml' package. Install with: pip install toml")
    else:
        raise InvalidFileFormatError("Unsupported file format. Use JSON, YAML, or TOML.")