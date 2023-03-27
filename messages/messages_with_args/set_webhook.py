import logging
from typing import List
from pymongo import MongoClient
from messages.message_interfaces import IMessage
from mocks.mock_mongo_client import MockMongoClient
from mocks.mock_requests import Requests
from decouple import config

class Webhook(IMessage):
    """Configures a webhook endpoint manually set by users for non reactive (CRON based) messaging.
    """
    def __init__(self, params: List[str], requests: Requests, mongo_client: MongoClient | MockMongoClient) -> None:
        __doc__ = IMessage.__init__.__doc__
        super().__init__(message="webhook", params=params, requests=requests, mongo_client=mongo_client)

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

        data = {"content": 'Attempting to add webhook...'}
        response = requests.post(webhook, json=data)
        self.logger.info(f"Attempted to configure webhook {webhook} with statuscode: {response.status_code}")
        if response.status_code < 200 or response.status_code > 208:
            return f"Could not register the webhook {webhook}, is the URL definitely correct?"

        webhook_db = self.mongo_client.get_database("webhook_db")
        webhooks = webhook_db.get_collection("webhooks")

        if webhook in [result["registered_webhook"] for result in webhooks.find()]:
            return f"The webhook {webhook} has already been registered, returning."

        try:
            webhooks.insert_one({"registered_webhook": webhook})
            return "Successfully added webhook to database!"
        except Exception as e:
            self.logger.warning(e.message)
            return "Something went wrong when inserting the webhook into the database, please try again..."

    def no_params_give_instructions(self) -> str:
        return "By setting up a webhook with a given channel, it means that we can send timer specific messages to it! It's very easy to do, " \
               "first click on the cog for a text channel, then click integrations and generate a webhook. You can then add a webhook to this " \
               "bot by running $webhook {the_webhook}!"
