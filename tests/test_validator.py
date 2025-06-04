import pytest
from config_validator import Schema, validate, ValidationError

def test_nested_structures():
    schema = Schema()
    schema.add_field("app.metadata.tags", list)
    config = {"app": {"metadata": {"tags": "production"}}}  # Невірний тип (str замість list)
    with pytest.raises(ValidationError):
        validate(config, schema)

def test_optional_field():
    schema = Schema()
    schema.add_field("optional_field", int, required=False)
    validate({}, schema)  # Не має викликати помилку