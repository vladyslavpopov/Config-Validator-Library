import pytest
from config_validator import Schema, validate, MissingFieldError, ValidationError

def test_schema_validation():
    schema = Schema()
    schema.add_field("name", str)
    schema.add_field("age", int, required=False)
    
    # Valid config
    assert validate({"name": "Alice"}, schema) is True
    
    # Missing required field
    with pytest.raises(MissingFieldError):
        validate({}, schema)
    
    # Invalid type
    with pytest.raises(ValidationError):
        validate({"name": 123}, schema)