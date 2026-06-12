import logging
import sys

def setup_logger(name: str = "book_admin_api") -> logging.Logger:
    """Configures and returns a centralized logger."""
    
    # Create logger
    logger = logging.getLogger(name)
    
    # If the logger is already configured, return it to avoid duplicate logs
    if logger.hasHandlers():
        return logger

    # Set the lowest severity level to log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    logger.setLevel(logging.INFO)

    # Create a console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    # Define the log format (Timestamp - Logger Name - Level - Message)

    
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(console_handler)

    return logger

# Initialize a global logger instance to be imported elsewhere
logger = setup_logger()