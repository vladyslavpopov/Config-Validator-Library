import os
from config_validator import Schema, parse_config, validate

# 1. Визначаємо шлях до конфігураційного файлу
current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, "complex_config.yaml")

# 2. Створення схеми валідації
schema = Schema()

# 2.1. Налаштування додатку
schema.add_field("app.name", str)
schema.add_field("app.debug", bool)
schema.add_field("app.ports", list)
schema.add_field("app.metadata.version", str)
schema.add_field("app.metadata.tags", list)

# 2.2. Налаштування бази даних
schema.add_field("database.primary.host", str)
schema.add_field("database.primary.credentials.username", str)
schema.add_field("database.primary.credentials.password", str)
schema.add_field("database.replica.host", str)
schema.add_field("database.replica.enabled", bool)

# 2.3. Налаштування логування
schema.add_field("logging.level", str)
schema.add_field("logging.handlers", list)

# 3. Парсинг та валідація
try:
    config = parse_config(config_path)
    validate(config, schema)
    print("Config is valid!")
except FileNotFoundError:
    print(f"Config file not found: {config_path}")
except Exception as e:
    print(f"Config validation failed: {e}")