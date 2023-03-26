from messages.message_interfaces import IMessage

class SayHello(IMessage):
    """An example class which sends "Hello there!" to a Discord channel when a user says hello.

    Args:
        IMessage (_type_): The Abstract base class.
    """
    def __init__(self, params) -> None:
        __doc__ = IMessage.__init__.__doc__
        super().__init__(message="test", params=params)

    def message_to_send(self) -> str:
        __doc__ = IMessage.message_to_send.__doc__
        return f"Hello there {' '.join(self.params)}!"
