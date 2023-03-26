import unittest
from messages.messages_no_args.hello import Hello

class TestHelloMessage(unittest.TestCase):
    """Tests the hello message package.
    """
    def test_hellopackage_sendsmessage(self) -> None:
        """Tests that the send_message command has the intended output.
        """
        self.assertEqual("Hello there mate!", Hello([]).message_to_send())
