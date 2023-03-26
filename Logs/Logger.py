import logging
import sys
from ast import List
from decouple import config

def initialize_logger(filename: str):
    """Initializes the logger with name "logger" for use in the bot, can turn of file writing by updating SHOULD_WRITE_LOGS
    in the .env file.

    Args:
        filename (str): The name of the file where loge outputs should be saved to.
    """
    args: List[str] = sys.argv[1:]
    instance = args[0]
    logger = logging.getLogger("logger")
    logger.setLevel(logging.DEBUG)

    channel_handler = logging.StreamHandler()
    channel_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(f"{instance[1:]} env - %(levelname)s:%(asctime)s: %(message)s")

    channel_handler.setFormatter(formatter)
    logger.addHandler(channel_handler)

    if config("SHOULD_WRITE_LOGS") == "true":
        file_handler = logging.FileHandler(filename)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
