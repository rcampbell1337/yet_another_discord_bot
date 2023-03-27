from typing import List
from logs.logger import initialize_logger
from decouple import config

def main():
    permitted_args: List[str] = ["test", "live"]
    args: str = config("ENVIRONMENT")

    if args not in permitted_args:
        raise Exception(f"Please specify one of the following environment variables when you run 'py main.py': {' ; '.join(permitted_args)}")
    initialize_logger(config("LOGGER_FILE"))
    import bot.bot

main()
