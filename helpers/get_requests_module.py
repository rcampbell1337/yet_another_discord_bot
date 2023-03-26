import sys
from typing import List
import requests as live_requests
from mocks.mock_requests import Requests as mock_requests

def get_requests_module():
    """Gets either the requests module for live use, or the requests Service.

    Returns:
        MockDiscordClient | Client: A model representing the requests module.
    """
    args: List[str] = sys.argv[1:]

    if len(args) == 1 and args[0] == "-test":
        return mock_requests()
    else:
        return live_requests
