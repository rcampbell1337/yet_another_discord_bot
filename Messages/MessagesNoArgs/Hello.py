from Messages.IMessage import IMessage

class Hello(IMessage):
    """An example class which sends "Hello there!" to a Discord channel when a user says hello.

    Args:
        IMessage (_type_): The Abstract base class.
    """
    def __init__(self) -> None:
        __doc__ = IMessage.__init__.__doc__
        super().__init__("hello")

    def message_to_send(self) -> str:
        __doc__ = IMessage.message_to_send.__doc__
        return "Hello there mate!"
