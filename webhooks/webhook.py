from abc import ABC, abstractmethod
from apscheduler.triggers.cron import CronTrigger
from typing import List
from mocks.mock_requests import Requests

class IWebhookMessage(ABC):
    """ Abstract base class representing an interaction which will send a message to Discord via a Channel Webhook.

    Args:
        ABC : The Abstract Base Class Restriction
    """
    def __init__(
        self,
        cron_trigger: CronTrigger,
        webhooks: List[str],
        requests: Requests,
    ) -> None:
        """ Constructor method.

        Args:
            message (str): The frequency that the function will be triggered.
            params (List[str]): A list of all of the channels to send messages to.
            params (requests | Requests): The mock or live requests module.
        """
        self.cron_trigger: CronTrigger = cron_trigger
        self.webhook: List[str] = webhooks
        self.requests = requests

    @abstractmethod
    def message_to_send(self) -> str:
        """ Creates a message to be sent to Discord via webhook.

        Returns:
            str: The message to be sent to Discord.
        """
        pass