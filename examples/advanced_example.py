import os
from config_validator import Schema, parse_config, validate

# 1. Визначаємо шлях до TOML-файлу
current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, "advanced_config.toml")

# 2. Створення схеми валідації
schema = Schema()
schema.add_field("app.name", str, regex=r"^[a-zA-Z0-9_]+$")
schema.add_field("app.port", int, min_value=1024, max_value=65535)
schema.add_list_field("app.hosts", str, min_length=1)
schema.add_field("database.host", str)
schema.add_field("database.port", int)

# 3. Кастомні валідатори
def validate_odd_port(port: int) -> bool:
    return port % 2 == 1

schema.add_validator("app.port", validate_odd_port)

# 4. Валідація
try:
    config = parse_config(config_path)
    validate(config, schema)
    print("Config is valid!")
except FileNotFoundError:
    print(f"File not found: {config_path}")
except Exception as e:
    print(f"Config validation failed: {e}")