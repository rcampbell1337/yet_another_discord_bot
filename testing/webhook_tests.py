import copy
import unittest
from messages.messages_with_args.set_webhook import Webhook
from mocks.mock_mongo_client import MockMongoClient
from mocks.mock_requests import Requests as mock_requests


class TestWebhook(unittest.TestCase):
    """Tests the hello message package.
    """
    @classmethod
    def setUpClass(self):
        self.requests = mock_requests()
        self.valid_webhook = "https://discord.com/api/webhooks/1089577542702333992/FDuO-Hdvasf_8sKyEoccZtcySYP97boXWubofaKL89GD4jd0IyM9jesU9t2ZzHCeDOWb"

    def test_noaddedparams_sendsinstructions(self) -> None:
        """Tests that when there are no params, instructions are given to the user.
        """
        self.assertEqual("By setting up a webhook with a given channel, it means that we can send timer specific messages to it! It's very easy to do, "
                         "first click on the cog for a text channel, then click integrations and generate a webhook. You can then add a webhook to this "
                         "bot by running $webhook {the_webhook}!", Webhook([], requests=self.requests, mongo_client=None).message_to_send())

    def test_morethanoneparam_sendserror(self) -> None:
        self.assertEqual("Please only enter the webhook URL and nothing else for the $webhook command.",
                         Webhook(["param1", "param2"], requests=self.requests, mongo_client=None).message_to_send())

    def test_webhookurldoesntstartcorrectly_sendserror(self) -> None:
        self.assertEqual("Please input a valid Discord Webhook.",
                         Webhook(["https://discord.com/api/wesbooks/1089577542702333992/FDuO-Hdvasf_8sKyEoccZtcySYP97boXWubofaKL89GD4jd0IyM9jesU9t2ZzHCeDOWb"],
                                 requests=self.requests, mongo_client=None).message_to_send())

    def test_incorrectwebhooklength_sendserror(self) -> None:
        self.assertEqual("Please input a valid Discord Webhook.",
                         Webhook(["https://discord.com/api/webhooks/108957754"], requests=self.requests, mongo_client=None).message_to_send())

    def test_postrequestrespondswithinvalidcode_sendserror(self) -> None:
        failed_request = copy.deepcopy(self.requests)
        failed_request.status_code = 400
        failed_request.response_message = "Failed"
        self.assertEqual(f"Could not register the webhook {self.valid_webhook}, is the URL definitely correct?",
                         Webhook([self.valid_webhook], requests=failed_request, mongo_client=None).message_to_send())

    def test_webhookalreadyexists_sendserror(self) -> None:
        mongo_client = MockMongoClient(None, {"registered_webhook": self.valid_webhook})
        self.assertEqual(f"The webhook {self.valid_webhook} has already been registered, returning.",
                         Webhook([self.valid_webhook], requests=self.requests, mongo_client=mongo_client).message_to_send())

    def test_newwebhook_getsinserted(self) -> None:
        mongo_client = MockMongoClient(None)
        self.assertEqual("Successfully added webhook to database!",
                         Webhook([self.valid_webhook], requests=self.requests, mongo_client=mongo_client).message_to_send())
