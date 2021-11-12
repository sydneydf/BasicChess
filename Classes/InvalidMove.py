class InvalidMove(Exception):
    failed: str = '\033[91m'
    endc: str = '\033[0m'

    def __init__(self, _message):
        super().__init__(_message)
        self.message = _message

    def __str__(self) -> str:
        return InvalidMove.failed + self.message + InvalidMove.endc
