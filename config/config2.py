import os
import logging.config
import yaml

os.makedirs("logs", exist_ok=True)

def setup_logging():
    with open("config/log_conf.yaml", "r") as file:
        config = yaml.safe_load(file)
        logging.config.dictConfig(config)
        
setup_logging()

