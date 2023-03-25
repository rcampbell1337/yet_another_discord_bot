from Helpers.GetDiscordClient import get_discord_client
from Messages.IMessage import IMessage
from decouple import config
from Messages.MessagesNoArgs.Hello import Hello

client = get_discord_client()

@client.event
async def on_ready():
    print("Bot is now online")

@client.event
async def on_message(message):
    for subclass in IMessage.__subclasses__():
        instance = subclass()
        if message.content == f"${instance.message}":
            await message.channel.send(instance.message_to_send())

token = config('DISCORD_TOKEN')
client.run(token)

