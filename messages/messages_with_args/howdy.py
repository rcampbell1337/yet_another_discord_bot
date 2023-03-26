from typing import List
from messages.message_interfaces import IMessage
from mocks.mock_mongo_client import MockMongoClient
from mocks.mock_requests import Requests

class Howdy(IMessage):
    """An example class which sends "Howdy {params}!" to a Discord channel when a user says .
    """
    def __init__(self, params: List[str], requests: Requests = None, mongo_client: MockMongoClient = None) -> None:
        __doc__ = IMessage.__init__.__doc__
        super().__init__(message="howdy", params=params, requests=requests, mongo_client=mongo_client)

    def message_to_send(self) -> str:
        __doc__ = IMessage.message_to_send.__doc__
        return f"Howdy {' '.join(self.params)}!"
