from logging import Logger
from Helpers.GetDiscordClient import get_discord_client
from Logs.Logger import get_logger
from Messages.IMessage import IMessage
from decouple import config
from Messages.MessagesNoArgs.Hello import Hello

client = get_discord_client()
logger = get_logger()

@client.event
async def on_ready():
    print("Bot is now online")

@client.event
async def on_message(message):
    for subclass in IMessage.__subclasses__():
        instance = subclass()
        if message.content == f"${instance.message}":
            logger.info(f"Sent message: {instance.message_to_send()}")
            await message.channel.send(instance.message_to_send())

token = config('DISCORD_TOKEN')
client.run(token)

