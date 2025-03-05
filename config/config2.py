import os
import logging.config
import yaml

config_path = os.path.join(os.path.dirname(__file__), "log_conf.yaml")


def setup_logging():
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
        logging.config.dictConfig(config)
        
setup_logging()

