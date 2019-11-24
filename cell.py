class Cell:
    def __init__(self, value):
        self._immutable = True if value > 0 else False
        self._value = value if self._immutable else None
        self.pencil = []
    def immutable(self):
        return self._immutable
    def set(self, _value):
        # Immutable after set
        assert self._immutable is False
        self._immutable = True
        self._value = _value
        self.pencil = []
    def get(self):
        return self._value
