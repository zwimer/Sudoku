from board import Board
from utilities import intersect
from utilities import trim

class Info:
    def __init__(self, b):
        self._board = b
        self._step = b.square_size()
        self._span = range(b.size())
    def get_allowed_in_col(self, x):
        vals = [ self._board.get(x,i) for i in self._span ]
        return self._missing(vals)
    def get_allowed_in_row(self, y):
        vals = [ self._board.get(i,y) for i in self._span ]
        return self._missing(vals)
    def get_allowed_in_square_of(self, x, y):
        xs = trim(x, self._step)
        ys = trim(y, self._step)
        n2 = self._step
        vals = [ self._board.get(i+xs,k+ys) for i in range(n2) for k in range(n2) ]
        return self._missing(vals)
    def get_allowed(self, x, y):
        a = self.get_allowed_in_col(x)
        b = self.get_allowed_in_row(y)
        c = self.get_allowed_in_square_of(x,y)
        return intersect(a, b, c)

    def _missing(self, vals):
        return [ i for i in self._board.range() if i not in vals ]
