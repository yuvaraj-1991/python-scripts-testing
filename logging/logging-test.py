from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler

# Step 1: Create logs directory
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# Step 2: Create application logger
logger = logging.getLogger("application")
logger.setLevel(logging.DEBUG)

# Step 3: Configure console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Step 4: Configure rotating file handler
file_handler = RotatingFileHandler(
    "logs/application.log",
    maxBytes=1024 * 1024,
    backupCount=3
)
file_handler.setLevel(logging.DEBUG)

# Step 5: Configure formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Step 6: Attach handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Step 7: Application execution
logger.info("Starting Application")

if log_dir.exists():
    logger.info("Log directory exists!")
else:
    logger.error("Log directory is missing!")

logger.info("Checking application health")
logger.info("Application execution completed")