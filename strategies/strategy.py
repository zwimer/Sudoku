class Strategy:
    def __init__(self, b):
        self._board = b
    def apply(self):
        pass
    def loop(self):
        changed = False
        while(self.apply()):
            changed = True
        return changed
