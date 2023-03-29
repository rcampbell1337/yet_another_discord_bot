from abc import ABC, abstractmethod
from typing import List
from discord import Guild
from pymongo import MongoClient
from mocks.mock_mongo_client import MockMongoClient
from mocks.mock_requests import Requests

class IMessage(ABC):
    """ Abstract base class representing an interaction which will send a message to Discord.

    Args:
        ABC : The Abstract Base Class Restriction
    """
    def __init__(
        self,
        server: Guild,
        message: str,
        params: List[str],
        requests: Requests = None,
        mongo_client: MongoClient | MockMongoClient = None
    ) -> None:
        """ Constructor method.

        Args:
            message (str): The message which will trigger this interaction.
            params (str): Any additional params in the message.
            params (requests | Requests): The mock or live requests module.
            params (MongoClient | MockMongoClient): The mock or live Mongo DB Client.
        """
        self.server: Guild = server
        self.message: str = message
        self.params: List[str] = params
        self.requests = requests
        self.mongo_client = mongo_client

    @abstractmethod
    def message_to_send(self) -> str:
        """ Creates a message to be sent to Discord.

        Returns:
            str: The message to be sent to Discord.
        """
        pass
