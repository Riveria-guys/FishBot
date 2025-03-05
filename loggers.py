import os
import logging.config
import yaml


def setup_logging():
    try:
        os.makedirs("logs", exist_ok=True)
        with open("config/log_conf.yaml", "r") as file:
            config = yaml.safe_load(file)
            logging.config.dictConfig(config)
    except Exception as err:
        print(err)
        