class InvalidMove(Exception):
    def __init__(self, _message):
        self.message = _message
        super(self).__init__(_message)

        def __str__(self) -> str:
            return self.message
