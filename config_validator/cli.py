import argparse
from pathlib import Path
from . import Schema, validate, parse_config

def main():
    parser = argparse.ArgumentParser(description='Config Validator CLI')
    parser.add_argument('--config', required=True, help='Path to config file')
    parser.add_argument('--schema', help='Path to schema file (YAML/JSON)')
    parser.add_argument('--format', choices=['json', 'yaml', 'toml'], help='Config file format')
    
    args = parser.parse_args()
    
    try:
        config = parse_config(args.config)
        schema = Schema()
        
        if args.schema:
            schema_data = parse_config(args.schema)
            _build_schema_from_dict(schema, schema_data)
        
        validate(config, schema)
        print("✅ Configuration is valid!")
    except Exception as e:
        print(f"❌ Validation failed: {e}")
        exit(1)

def _build_schema_from_dict(schema: Schema, schema_data: dict) -> None:
    for field, rules in schema_data.get('fields', {}).items():
        field_type = eval(rules['type']) if isinstance(rules['type'], str) else rules['type']
        schema.add_field(
            name=field,
            field_type=field_type,
            required=rules.get('required', True),
            min_value=rules.get('min'),
            max_value=rules.get('max'),
            regex=rules.get('regex')
        )