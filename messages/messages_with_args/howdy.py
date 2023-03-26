from typing import List
from messages.message_interfaces import IMessage

class Howdy(IMessage):
    """An example class which sends "Howdy {params}!" to a Discord channel when a user says .
    """
    def __init__(self, params: List[str]) -> None:
        __doc__ = IMessage.__init__.__doc__
        super().__init__(message="howdy", params=params)

    def message_to_send(self) -> str:
        __doc__ = IMessage.message_to_send.__doc__
        return f"Howdy {' '.join(self.params)}!"
