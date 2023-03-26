import logging
from helpers.get_discord_client import get_discord_client
from messages.message_interfaces import IMessage
from decouple import config
from messages.messages_no_args.hello import Hello
from messages.messages_with_args.say_hello import SayHello

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
    for subclass in IMessage.__subclasses__():
        message_content = message.content.split(" ")
        instance = subclass(params=message_content[1:])
        if message_content[0] == f"${instance.message}":
            logger.info(f"Sent message: {instance.message_to_send()}")
            await message.channel.send(instance.message_to_send())

token = config('DISCORD_TOKEN')
client.run(token)
