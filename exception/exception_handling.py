import logging
from logger.logging import get_logger

logger = get_logger()

class AITripPlannerError(Exception):
    """Base exception class for AI Trip Planner."""

    def __init__(self, message=None):
        super().__init__(message)
        logger.error(f"AITripPlannerError: {message}")


class APIError(AITripPlannerError):
    """Exception for API related errors."""

    def __init__(self, api_name, message="API request failed"):
        error_message = f"{api_name} APIError: {message}"
        super().__init__(error_message)


class ConfigurationError(AITripPlannerError):
    """Exception raised for configuration loading errors."""

    def __init__(self, message="Configuration error occurred"):
        super().__init__(message)


class DataNotFoundError(AITripPlannerError):
    """Exception raised when expected data is not found."""

    def __init__(self, data_name="Data", message=None):
        if message is None:
            message = f"{data_name} not found"
        super().__init__(message)


class ValidationError(AITripPlannerError):
    """Exception raised for validation issues."""

    def __init__(self, field_name, message=None):
        if message is None:
            message = f"Invalid value for field '{field_name}'"
        super().__init__(message)
