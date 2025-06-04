import os
from config_validator import Schema, parse_config, validate

# Полный путь к файлу конфигурации
config_path = os.path.join(os.path.dirname(__file__), "basic_config.json")

# Создаем схему
schema = Schema()
schema.add_field("database", dict)
schema.add_field("database.host", str)
schema.add_field("database.port", int)
schema.add_field("debug", bool, required=False)

# Проверяем конфигурацию
try:
    config = parse_config(config_path)
    validate(config, schema)
    print("Config is valid!")
except Exception as e:
    print(f"Config validation failed: {e}")