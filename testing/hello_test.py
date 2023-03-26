import unittest
from messages.messages_no_args.hello import Hello

class TestHelloMessage(unittest.TestCase):
    def test_response(self):
        self.assertEqual("Hello there mate!", Hello().message_to_send())
