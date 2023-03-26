import asyncio
from typing import Any, Callable, Coroutine, TypeVar
from Logs.Logger import get_logger

T = TypeVar('T')
Coro = Coroutine[Any, Any, T]
CoroT = TypeVar('CoroT', bound=Callable[..., Coro[Any]])

class MockDiscordClient:
    _coro_list = []

    def __init__(self):
        self.logger = get_logger()

    async def start(self, token: str, *, reconnect: bool = True) -> None:
        while True:
            selected_func = list(filter(lambda coro: coro.__name__ == "on_message", self._coro_list))[0]
            if selected_func.__name__ == "on_message":
                self.logger.debug("Enter a message to test: ")
                message = input()
                message_obj = Message(message)
                await selected_func(message_obj)


    def run(
        self,
        token: str,
        *,
        reconnect: bool = True,
    ) -> None:
        async def runner():
            await self.start(token)

        try:
            asyncio.run(runner())
        except KeyboardInterrupt:
            return

    def event(self, coro: CoroT, /) -> None:
        if not asyncio.iscoroutinefunction(coro):
            raise TypeError('event registered must be a coroutine function')

        setattr(self, coro.__name__, coro)
        self._coro_list.append(coro)

class Message:
    def __init__(self, content):
        self.content = content
        self.channel = Channel()

class Channel:
    async def send(self, message: str):
        pass