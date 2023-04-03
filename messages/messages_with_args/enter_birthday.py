import logging
from urllib.parse import quote
from typing import List
from decouple import config
from discord import Guild
from pymongo import MongoClient
from messages.message_interfaces import IMessage
from mocks.mock_mongo_client import MockMongoClient
from mocks.mock_requests import Requests

class Webhook(IMessage):
    """Configures a webhook endpoint manually set by users for non reactive (CRON based) messaging.
    """
    def __init__(self, server: Guild, params: List[str], requests: Requests, mongo_client: MongoClient | MockMongoClient) -> None:
        __doc__ = IMessage.__init__.__doc__
        super().__init__(server=server, message="birthday", params=params, requests=requests, mongo_client=mongo_client)

        self.logger = logging.getLogger("logger")
        self.mongo_client = mongo_client

    def message_to_send(self) -> str:
        __doc__ = IMessage.message_to_send.__doc__

        webhook_db = self.mongo_client.get_database("webhook_db")
        webhooks = webhook_db.get_collection("webhooks")
        webhook_set = len(list(webhooks.find({"server": self.server.id}))) == 1

        if not webhook_set:
            return f"By setting up a webhook with a given channel, it means that we can send timer specific messages to it! It's very easy to do, " \
                   f"first click on the cog for a text channel, then click integrations and generate a webhook. You can then add a webhook to this " \
                   f"bot by going to this URL: {config('HOSTNAME')}?id={self.server.id}&discord_server_name={quote(self.server.name)} !"
        
        return f"Follow this link to enter your server birthday! {config('HOSTNAME')}?id={self.server.id}&discord_server_name={quote(self.server.name)} !"
