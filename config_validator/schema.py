from typing import Any, Dict, List, Union, Callable
from config_validator.exceptions import ValidationError


class Schema:
    def __init__(self):
        self.fields: Dict[str, Dict[str, Any]] = {}
        self.validators: Dict[str, List[Callable]] = {}
        self.conditionals: List[Dict[str, Any]] = []

    def add_field(
        self,
        name: str,
        field_type: type,
        *,
        required: bool = True,
        min_value: Union[int, float, None] = None,
        max_value: Union[int, float, None] = None,
        regex: Union[str, None] = None,
        custom_validator: Union[Callable, None] = None
    ) -> None:
        self.fields[name] = {
            'type': field_type,
            'required': required,
            'min': min_value,
            'max': max_value,
            'regex': regex,
            'custom': custom_validator
        }

    def add_list_field(
        self,
        name: str,
        item_type: type,
        *,
        required: bool = True,
        min_length: Union[int, None] = None,
        max_length: Union[int, None] = None
    ) -> None:
        self.fields[name] = {
            'type': list,
            'item_type': item_type,
            'required': required,
            'min_length': min_length,
            'max_length': max_length,
            'custom': None 
        }

    def add_conditional(
        self,
        field: str,
        condition_field: str,
        condition_value: Any,
        field_type: type,
        required: bool = True
    ) -> None:
        self.conditionals.append({
            'field': field,
            'condition_field': condition_field,
            'condition_value': condition_value,
            'type': field_type,
            'required': required
        })

    def add_validator(self, field: str, validator: Callable) -> None:
        if field not in self.validators:
            self.validators[field] = []
        self.validators[field].append(validator)