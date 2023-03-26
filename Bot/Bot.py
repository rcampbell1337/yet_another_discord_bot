import logging
from Helpers.GetDiscordClient import get_discord_client
from Messages.IMessage import IMessage
from decouple import config
from Messages.MessagesNoArgs.Hello import Hello

client = get_discord_client()
logger = logging.getLogger("logger")

@client.event
async def on_ready() -> None:
    """Triggered when the live service is turned on.
    """
    logger.info("Bot is now online")

@client.event
async def on_message(message) -> None:
    """Triggered when a Discord message is sent to a channel.

    Args:
        message (str): The message that has triggered the event.
    """
    for subclass in IMessage.__subclasses__():
        instance = subclass()
        if message.content == f"${instance.message}":
            logger.info(f"Sent message: {instance.message_to_send()}")
            await message.channel.send(instance.message_to_send())

token = config('DISCORD_TOKEN')
client.run(token)
