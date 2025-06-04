class ConfigError(Exception):
    pass

class ValidationError(ConfigError):
    pass

class MissingFieldError(ConfigError):
    pass

class InvalidFileFormatError(ConfigError):
    pass