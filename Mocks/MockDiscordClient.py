import asyncio
import logging
from typing import Any, Callable, Coroutine, TypeVar

T = TypeVar('T')
Coro = Coroutine[Any, Any, T]
CoroT = TypeVar('CoroT', bound=Callable[..., Coro[Any]])
logger = logging.getLogger("logger")

class MockDiscordClient:
    """Mock client representing the Discord Bot service, used for local development not connected to any of the live Discord Services.
    """

    # Stores all coroutines registered as Discord events.
    _coro_list = []

    async def start(self, token: str, *, reconnect: bool = True) -> None:
        """When the Mock Service has been fully initialized, this method is run and allows for the entry of mock discord messages.

        Args:
            token (str): Necessary for overloading default Discord meth.
            reconnect (bool, optional): Necessary for overloading default Discord meth. Defaults to True.
        """
        while True:
            selected_func = list(filter(lambda coro: coro.__name__ == "on_message", self._coro_list))[0]
            if selected_func.__name__ == "on_message":
                logger.debug("Enter a message to test: ")
                message = input()
                message_obj = Message(message)
                await selected_func(message_obj)

    def run(
        self,
        token: str,
        *,
        reconnect: bool = True,
    ) -> None:
        """Runs the discord bot service and keeps it alive for testing.

        Args:
            token (str): Necessary for overloading default Discord meth.
            reconnect (bool, optional): Necessary for overloading default Discord meth. Defaults to True.
        """
        async def runner():
            await self.start(token)

        try:
            asyncio.run(runner())
        except KeyboardInterrupt:
            return

    def event(self, coro: CoroT, /) -> None:
        """Registers the coroutines which represent the Discord events, this can then be used to mock calling them in the command line.

        Args:
            coro (CoroT): The coroutine being passed in.

        Raises:
            TypeError: If the type being passed in is not a coroutine.
        """
        if not asyncio.iscoroutinefunction(coro):
            raise TypeError('event registered must be a coroutine function')

        setattr(self, coro.__name__, coro)
        self._coro_list.append(coro)

class Message:
    """Represents a Discord Message Object.
    """
    def __init__(self, content):
        """Constructor Method
        """
        self.content = content
        self.channel = Channel()

class Channel:
    """Mocks the channel object on a message (to facilitate the sending of messages).
    """
    async def send(self, message: str, should_log=False):
        """Mocks the sending of a message to a Discord Channel.

        Args:
            message (str): The message to be sent.
            should_log (bool, optional): Whether this should be output in the logs. Defaults to False as is done in the on_message method presently.
        """
        if should_log:
            logger.debug(message)
        pass
