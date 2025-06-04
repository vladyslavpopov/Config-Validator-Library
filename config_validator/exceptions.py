class ConfigError(Exception):
    """Base exception for all config-related errors."""
    pass

class ValidationError(ConfigError):
    """Raised when a field fails validation."""
    pass

class MissingFieldError(ConfigError):
    """Raised when a required field is missing."""
    pass

class InvalidFileFormatError(ConfigError):
    """Raised when an unsupported file format is provided."""
    pass