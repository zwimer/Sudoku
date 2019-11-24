from info import Info
from strategy import Strategy
from utilities import intersect

class Simple(Strategy):
    def apply(self):
        board = self._board
        info = Info(board)
        step = board.size()
        change = False
        for x in range(step):
            for y in range(step):
                if board.immutable(x,y):
                    continue
                chk = info.get_allowed(x,y)
                get_pen = board.pencil(x,y)
                pen = intersect(get_pen, chk)
                assert len(chk) > 0
                assert len(pen) > 0
                if len(pen) < len(get_pen):
                    change = True
                if len(pen) == 1:
                    board.set(x, y, pen[0])
                    change = True
                else:
                    board.set_pencil(x,y,pen)
        return change
