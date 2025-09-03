import logging
import os
from logging.handlers import RotatingFileHandler

# Create logs directory if it does not exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Log file path
LOG_FILE = os.path.join(LOG_DIR, "ai_trip_planner.log")

# Logger configuration
logger = logging.getLogger("AI_Trip_Planner_Logger")
logger.setLevel(logging.DEBUG)  # Capture all levels DEBUG and above

# RotatingFileHandler for log rotation (max 5MB per file, keep 3 backups)
file_handler = RotatingFileHandler(LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=3)
file_handler.setLevel(logging.DEBUG)

# Console handler for output to terminal
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Adjust as needed

# Log format
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def get_logger():
    """Return the configured logger instance."""
    return logger
