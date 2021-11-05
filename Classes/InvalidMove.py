class InvalidMove(Exception):
    def __init__(self, _message):
        super().__init__(_message)
        self.message = _message

    def __str__(self) -> str:
        return self.message
