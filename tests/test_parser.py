import pytest
from config_validator import parse_config, InvalidFileFormatError

def test_parse_json(tmp_path):
    config_file = tmp_path / "test.json"
    config_file.write_text('{"key": "value"}')
    assert parse_config(str(config_file)) == {"key": "value"}

def test_parse_invalid_format(tmp_path):
    config_file = tmp_path / "test.txt"
    config_file.write_text("key=value")
    with pytest.raises(InvalidFileFormatError):
        parse_config(str(config_file))