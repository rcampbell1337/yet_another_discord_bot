from typing import List
from messages.message_interfaces import IMessage

class Hello(IMessage):
    """An example class which sends "Hello there!" to a Discord channel when a user says hello.

    Args:
        IMessage (_type_): The Abstract base class.
    """
    def __init__(self, params: List[str]) -> None:
        __doc__ = IMessage.__init__.__doc__
        super().__init__(message="hello", params=params)

    def message_to_send(self) -> str:
        __doc__ = IMessage.message_to_send.__doc__
        return "Hello there mate!"
