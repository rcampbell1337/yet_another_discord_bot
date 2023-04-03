import dataclasses
import unittest
from messages.messages_with_args.enter_birthday import Webhook

@dataclasses.dataclass
class Guild:
    id: str
    name: str

class TestWebhook(unittest.TestCase):
    """Tests the hello message package.
    """
    def test_noaddedparams_sendsinstructions(self) -> None:
        """Tests that when there are no params, instructions are given to the user.
        """
        self.assertIn("By setting up a webhook with a given channel, it means that we can send timer specific messages to it! It's very easy to do, "
                      "first click on the cog for a text channel, then click integrations and generate a webhook. You can then add a webhook to this "
                      "bot by going to this URL:", Webhook(Guild(id="123", name="123"), [], requests=None, mongo_client=None).message_to_send())
