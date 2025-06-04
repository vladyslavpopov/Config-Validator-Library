from typing import Dict, Any
from config_validator.exceptions import ValidationError, MissingFieldError  # Абсолютний імпорт
from config_validator.schema import Schema  # Абсолютний імпорт

def validate(config: Dict[str, Any], schema: 'Schema') -> bool:
    for field, rules in schema.fields.items():
        # Проверка вложенных полей
        if '.' in field:
            parts = field.split('.')
            current = config
            for part in parts[:-1]:
                if part not in current:
                    if rules["required"]:
                        raise MissingFieldError(f"Missing required field: {field}")
                    break
                current = current[part]
            else:
                if not isinstance(current.get(parts[-1]), rules["type"]):
                    raise ValidationError(
                        f"Field '{field}' must be of type {rules['type'].__name__}, "
                        f"got {type(current.get(parts[-1])).__name__} instead."
                    )
        else:
            if rules["required"] and field not in config:
                raise MissingFieldError(f"Missing required field: {field}")
            if field in config and not isinstance(config[field], rules["type"]):
                raise ValidationError(
                    f"Field '{field}' must be of type {rules['type'].__name__}, "
                    f"got {type(config[field]).__name__} instead."
                )
    return True