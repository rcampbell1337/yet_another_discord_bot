import logging
from helpers.live_or_mock_service import LiveOrMockService
from decouple import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# Register all Discord Message triggered functions.
from messages.message_interfaces import IMessage
from messages.messages_no_args.hello import Hello
from messages.messages_with_args.howdy import Howdy
from messages.messages_with_args.set_webhook import Webhook

# Register all timer triggered discord functions.
from webhooks.webhook import IWebhookMessage
from webhooks.test import Test

# Configure the external services to be either live or mocked, and get the logger.
live_or_mock_service = LiveOrMockService(config("MONGO_DB_CONN_URL"))
client = live_or_mock_service.discord_client
requests = live_or_mock_service.requests
mongo_client = live_or_mock_service.mongo_client
logger = logging.getLogger("logger")

@client.event
async def on_ready() -> None:
    """Triggered when the -live service is turned on.
    """
    logger.info("Bot is now online")
    sched = AsyncIOScheduler()
    sched.start()
    for subclass in IWebhookMessage.__subclasses__():
        instance = subclass(webhooks=[], requests=requests)
        sched.add_job(func=instance.message_to_send, trigger=instance.cron_trigger, id=instance.name)
        logger.info(f"Successfully registered webhook: {instance.__class__} on interval {instance.cron_trigger}")
        sched.remove_job(instance.name)

@client.event
async def on_message(message) -> None:
    """Triggered when a Discord message is sent to a channel.

    Args:
        message (str): The message that has triggered the event.
    """
    enabled_messages = config("ENABLED_MESSAGES").split(",")
    message_content = message.content.split(" ")
    if message_content[0][1:] not in enabled_messages:
        return

    for subclass in IMessage.__subclasses__():
        instance = subclass(params=message_content[1:], requests=requests, mongo_client=mongo_client)
        if message_content[0] == f"${instance.message}":
            message_to_send = instance.message_to_send()
            if not message_to_send or len(message_to_send) == 0:
                return

            await message.channel.send(message_to_send)
            logger.info(f"Sent message: {message_to_send}")

token = config('DISCORD_TOKEN')
client.run(token)
