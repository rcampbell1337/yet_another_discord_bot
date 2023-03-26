from abc import ABC, abstractmethod
from typing import List

class IMessage(ABC):
    """ Abstract base class representing an interaction which will send a message to Discord.

    Args:
        ABC : The Abstract Base Class Restriction
    """
    def __init__(self, message: str, params: List[str]) -> None:
        """ Constructor method.

        Args:
            message (str): The message which will trigger this interaction.
            params (str): Any additional params in the message.
        """
        self.message: str = message
        self.params: List[str] = params

    @abstractmethod
    def message_to_send(self) -> str:
        """ Creates a message to be sent to Discord.

        Returns:
            str: The message to be sent to Discord.
        """
        pass
