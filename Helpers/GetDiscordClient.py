import sys
from typing import List
import discord
from Mocks.MockDiscordClient import MockDiscordClient


def get_discord_client():
    args: List[str] = sys.argv[1:]

    if len(args) == 1 and args[0] == "-test":
        return MockDiscordClient()
    else:
        return discord.Client(intents=discord.Intents.all())