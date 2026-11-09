#Hello we are trying to create an automation script for logging. 
#Imagine you write a Python script that checks whether your production application is healthy.

from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler

#Step1 - create a logs Path object and dir
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

#Step3 - Creating a application logger and setting all 5 levels
logger = logging.getLogger('application')
logger.setLevel(logging.DEBUG)

#step 4 Console handler - this will send messages to terminal 

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

#step5 Configure rotating files with filehandlers and this is because we dont want files to grow indefenitly

file_handler = RotatingFileHandler("logs/application.log",maxBytes=1024*1024,backupCount=3)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

#Step 6 - configure the formatter to display messages in format 

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#Step 7 attach both handles to same formatter for logs and files
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)


#Start application logs

logger.info("Starting Application")

#Step2 check whether dir exists
if log_dir.exists():
    logger.info("Log directory exists!")
else:
    logger.error("Log Directory is missing!!!!")

logger.info("Checking application health")

logger.info("Application execution completed")



logger.debug("Debugging application")
logger.info("Application running normally")
logger.warning("Application response is slow")
logger.error("Application encountered an error")
logger.critical("Critical application failure")
