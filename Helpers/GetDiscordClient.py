import sys
from typing import List
import discord


def get_discord_client():
    args: List[str] = sys.argv[1:]

    if len(args) == 1 and args[0] == "-test":
        # TODO
        return None
    else:
        intents = discord.Intents.all()
        return discord.Client(intents=intents)