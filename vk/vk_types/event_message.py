"""Event message object."""


class EventMessage:
    """Event message class."""

    def __init__(self, type, msg_id, flags, peer, value, title, text, **kwargs) -> None:  # noqa: D107
        self.type = type
        self.msg_id = msg_id
        self.flags = flags
        self.chat_id = peer
        self.text = text
        self.title = title
        self.__dict__.update(kwargs)

    def __repr__(self) -> str:
        return f"from {self.title}: {self.text}, chat id: {self.chat_id}"
