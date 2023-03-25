import sys
import Bot.Bot
from typing import List

def main():
    permitted_args: List[str] = ["-test", "-live"]
    args: List[str] = sys.argv[1:]

    if len(args) != 1 or args[0] not in permitted_args:
        raise Exception(f"Please specify one of the following Keywords when you run 'py main.py': {' ; '.join(permitted_args)}")

if __name__ == "__main__":
    main()

