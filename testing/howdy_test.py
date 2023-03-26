import unittest
from messages.messages_with_args.howdy import Howdy

class TestHelloMessage(unittest.TestCase):
    """Tests the howdy message package.
    """
    def test_standard_msg(self) -> None:
        self.assertEqual("Howdy big man!", Howdy(["big", "man"]).message_to_send())

    def test_empty_content(self) -> None:
        self.assertEqual("Howdy !", Howdy([]).message_to_send())
