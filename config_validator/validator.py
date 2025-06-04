import re
from typing import Any, Dict
from config_validator.exceptions import ValidationError, MissingFieldError
from config_validator.schema import Schema

def validate(config: Dict[str, Any], schema: Schema) -> bool:
    # Перевірка основних полів
    for field, rules in schema.fields.items():
        value = _get_nested(config, field)
        
        if rules['required'] and value is None:
            raise MissingFieldError(f"Missing required field: {field}")
            
        if value is not None:
            _validate_field(field, value, rules)
    
    # Перевірка умовних полів
    for condition in schema.conditionals:
        if _get_nested(config, condition['condition_field']) == condition['condition_value']:
            value = _get_nested(config, condition['field'])
            if condition['required'] and value is None:
                raise MissingFieldError(f"Conditional field {condition['field']} is required when {condition['condition_field']} == {condition['condition_value']}")
    
    # Кастомні валідатори
    for field, validators in schema.validators.items():
        value = _get_nested(config, field)
        for validator in validators:
            if not validator(value):
                raise ValidationError(f"Validation failed for field {field}")

    return True

def _get_nested(config: Dict[str, Any], path: str) -> Any:
    keys = path.split('.')
    current = config
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None
    return current

def _validate_field(field: str, value: Any, rules: Dict[str, Any]) -> None:
    # Перевірка типу
    if not isinstance(value, rules['type']):
        raise ValidationError(f"Field '{field}' must be of type {rules['type'].__name__}")
    
    # Перевірка діапазону для чисел
    if isinstance(value, (int, float)):
        if rules['min'] is not None and value < rules['min']:
            raise ValidationError(f"Field '{field}' must be ≥ {rules['min']}")
        if rules['max'] is not None and value > rules['max']:
            raise ValidationError(f"Field '{field}' must be ≤ {rules['max']}")
    
    # Перевірка регулярного виразу
    if isinstance(value, str) and rules['regex']:
        if not re.match(rules['regex'], value):
            raise ValidationError(f"Field '{field}' doesn't match required pattern")
    
    # Кастомна валідація
    if rules['custom'] and not rules['custom'](value):
        raise ValidationError(f"Custom validation failed for field {field}")