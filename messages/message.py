from abc import ABC, abstractmethod

class IMessage(ABC):
    """ Abstract base class representing an interaction which will send a message to Discord.

    Args:
        ABC : The Abstract Base Class Restriction
    """
    def __init__(self, message: str) -> None:
        """ Constructor method.

        Args:
            message (str): The message which will trigger this interaction.
        """
        self.message: str = message

    @abstractmethod
    def message_to_send(self) -> str:
        """ Creates a message to be sent to Discord.

        Returns:
            str: The message to be sent to Discord.
        """
        pass
