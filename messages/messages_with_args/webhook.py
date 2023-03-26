import logging
from typing import List
from messages.message_interfaces import IMessage
from mocks.mock_mongo_client import MockMongoClient
from mocks.mock_requests import Requests

class Webhook(IMessage):
    """Configures a webhook endpoint manually set by users for non reactive (CRON based) messaging.

    Args:
        IMessage (_type_): The Abstract base class.
    """
    def __init__(self, params: List[str], requests: Requests, database: MockMongoClient) -> None:
        __doc__ = IMessage.__init__.__doc__
        super().__init__(message="webhook", params=params, requests=requests, database=database)

        self.logger = logging.getLogger("logger")

    def message_to_send(self) -> str:
        __doc__ = IMessage.message_to_send.__doc__
        if len(self.params) == 0:
            return self.no_params_give_instructions()

        if len(self.params) != 1:
            return "Please only enter the webhook URL and nothing else for the $webhook command."

        requests = self.requests
        webhook = self.params[0]

        if "https://discord.com/api/webhooks/" not in webhook or len(webhook) != 121:
            return "Please input a valid Discord Webhook."

        data = {"content": 'Webhook has been added! (You can delete the previous message now)'}
        response = requests.post(webhook, json=data)
        self.logger.info(f"Attempted to configure webhook {webhook} with statuscode: {response.status_code}")
        if response.status_code < 200 or response.status_code > 208:
            return "Could not register the webhook, is the URL definitely correct?"

        database = self.database
        print(database)

    def no_params_give_instructions(self) -> str:
        return "By setting up a webhook with a given channel, it means that we can send timer specific messages to it! It's very easy to do, " \
               "first click on the cog for a text channel, then click integrations and generate a webhook. You can then add a webhook to this " \
               "bot by running $webhook {the_webhook}!"
