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
        name: str,
        webhooks: List[str],
        requests: Requests,
    ) -> None:
        """ Constructor method.

        Args:
            cron_trigger (str): The frequency that the function will be triggered.
            name (str): The name representing the webhook (used to remove job from scheduler).
            webhooks (List[str]): A list of all of the channels to send messages to.
            requests (requests | Requests): The mock or live requests module.
        """
        self.cron_trigger: CronTrigger = cron_trigger
        self.webhook: List[str] = webhooks
        self.requests = requests
        self.name = name

    @abstractmethod
    def message_to_send(self) -> str:
        """ Creates a message to be sent to Discord via webhook.

        Returns:
            str: The message to be sent to Discord.
        """
        pass