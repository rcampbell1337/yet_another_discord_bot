import discord
from discord.ext import commands
from Messages.IMessage import IMessage
from Messages.MessagesNoArgs.Hello import Hello

class Bot(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='$', self_bot=False, intents=intents)
        self.add_commands()

    async def on_ready(self):
        print("Bot is now online")

    def add_commands(self):
        for subclass in IMessage.__subclasses__():
            instance = subclass()
            @self.command(name=instance.message, pass_context=True)
            async def command(ctx):
                await ctx.send(instance.message_to_send())
