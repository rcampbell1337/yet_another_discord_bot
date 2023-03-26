import logging

logger = logging.getLogger("logger")
logger.setLevel(logging.DEBUG)

channel_handler = logging.StreamHandler()
channel_handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('./Logs/logs.log')
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s:%(asctime)s:%(message)s")

channel_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
logger.addHandler(channel_handler)
logger.addHandler(file_handler)

def get_logger():
    return logger
