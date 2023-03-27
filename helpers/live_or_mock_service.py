import requests as live_requests
import discord
from dataclasses import dataclass
from mocks.mock_mongo_client import MockMongoClient
from mocks.mock_discord_client import MockDiscordClient
from mocks.mock_requests import Requests as mock_requests
from pymongo import MongoClient
from decouple import config

@dataclass
class LiveOrMockService:
    def __init__(self, connection_url: str):
        args: str = config("ENVIRONMENT")

        if args == "test":
            self.discord_client = MockDiscordClient()
            self.requests = mock_requests()
            self.mongo_client = MockMongoClient(connection_url)
        else:
            self.discord_client = discord.Client(intents=discord.Intents.all())
            self.requests = live_requests
            self.mongo_client = MongoClient(connection_url)
