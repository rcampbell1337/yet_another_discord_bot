import unittest
from messages.messages_with_args.howdy import Howdy

class TestHelloMessage(unittest.TestCase):
    """Tests the howdy message package.
    """
    def test_standardmsg_sendsmessage(self) -> None:
        self.assertEqual("Howdy big man!", Howdy(None, ["big", "man"], None, None).message_to_send())

    def test_emptycontent_sendsmessage(self) -> None:
        self.assertEqual("Howdy !", Howdy(None, [], None, None).message_to_send())
