import sys
from typing import List
from Live.Bot import Bot
from Testing.Test import Test

if __name__ == "__main__":
    permitted_args: List[str] = ["-test", "-live"]
    args: List[str] = sys.argv[1:]

    if len(args) != 1 or args[0] not in permitted_args:
        raise Exception(f"Please specify one of the following Keywords when you run 'py main.py': {' ; '.join(permitted_args)}")

    if (args[0] == "-test"):
        Test()

    if args[0] == "-live":
        Bot()
