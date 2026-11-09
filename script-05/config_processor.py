#Here we will create a script to check JSON configuration before deploying application

import json
import logging
import sys
from pathlib import Path

conf_file = Path('config.json')

logger = logging.getLogger('config_processor')
logger.setLevel(logging.DEBUG)

class ConfigurationError(Exception):
    pass

required_keys = [
    "application",
    "environment",
    "replicas",
    "port"
]

try:
    with open(conf_file , 'r') as fil:
        json_config_file = json.load(fil)
        for key in required_keys:
            if key not in json_config_file:
                raise ConfigurationError(f"Missing required configuration: {key}")
                
        
except FileNotFoundError:
    logger.error("Configuration file not found!") 
    sys.exit(1)        
except PermissionError:
    logger.error("File Permission Denied!") 
    sys.exit(1) 
except json.JSONDecodeError:
    logger.error("Invalid JSON configuration")    
    sys.exit(1)  
except ConfigurationError as e:
    logger.error("Configuration validation failed: %s", e)
    sys.exit(1) 

else:
    logger.info("Configuration Loading")    
    logger.debug(json_config_file)
    sys.exit(0) 

finally:
    logger.info("Configuration processing completed")    