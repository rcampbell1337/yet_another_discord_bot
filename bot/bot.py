import logging
from helpers.get_discord_client import get_discord_client
from messages.message_interfaces import IMessage
from decouple import config
from messages.messages_no_args.hello import Hello
from messages.messages_with_args.howdy import Howdy
from messages.messages_with_args.webhook import Webhook

client = get_discord_client()
logger = logging.getLogger("logger")

@client.event
async def on_ready() -> None:
    """Triggered when the -live service is turned on.
    """
    logger.info("Bot is now online")

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
        instance = subclass(params=message_content[1:])
        if message_content[0] == f"${instance.message}":
            message_to_send = instance.message_to_send()
            if len(message_to_send) == 0:
                return
            
            await message.channel.send(message_to_send)
            logger.info(f"Sent message: {message_to_send}")

token = config('DISCORD_TOKEN')
client.run(token)
