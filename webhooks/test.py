from apscheduler.triggers.cron import CronTrigger
from typing import List
from mocks.mock_requests import Requests
from webhooks.webhook import IWebhookMessage


class Test(IWebhookMessage):
    def __init__(self, webhooks: List[str], requests: Requests) -> None:
        super().__init__(cron_trigger=CronTrigger(day="*", hour="12", minute="*", second="*"), name="test", webhooks=webhooks, requests=requests)

    def message_to_send(self) -> None:
        print("Registered CRON job")
