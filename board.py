from copy import deepcopy
from math import sqrt
from cell import Cell

class Board:
    # Access board by col, then row: board[x][y]

    @classmethod
    def load(cls, fname):
        with open(fname) as f:
            data = [ i.strip() for i in f.readlines() if i ]
        assert len(data) == 9
        assert len(data[0]) == 9
        data = [ [ int(k) for k in list(i) ] for i in data ]
        return cls(data)
    def save(self, fname):
        n = self.size()
        assert n == 9
        vals = [ [ self.get(x,y) for x in range(n) ] for y in range(n) ]
        def to_str(x):
            return str(x) if x is not None else '0'
        vals = [ [ to_str(x) for x in y ] for y in vals ]
        outs = '\n'.join([ ''.join(i) for i in vals ])
        with open(fname, 'w') as f:
            f.write(outs)

    def __init__(self, grid):
        # Grid import by row then col: grid[y][x]
        self._n = len(grid)
        self._n2 = int(sqrt(self._n))
        assert self._n == 9
        assert self._n2 == 3
        assert self._n == len(grid[0])
        self._board = [ [ Cell(grid[k][i]) for k in range(self._n) ] for i in range(self._n) ]
        self._range = range(1, 1 + self._n)

    def immutable(self, x, y):
        return self._board[x][y].immutable()
    def get(self, x, y):
        return self._board[x][y].get()
    def set(self, x, y, v):
        print "set(", str(x+1), ",", str(y+1), ",", str(v), ")"
        self._board[x][y].set(v)
    def range(self):
        return self._range

    def pencil(self, x, y):
        return [] if self.immutable(x,y) else self._board[x][y].pencil
    def set_pencil(self, x, y, p):
        if not self.immutable(x,y):
            self._board[x][y].pencil = p

    def square_size(self):
        return self._n2
    def size(self):
        return self._n

    def pnt(self):
        n = self._n
        n2 = self._n2
        assert n == 9
        assert n2 == 3

        dash = u'\u2013'
        block = u'\u2588'
        solid_line = block*(4*n+n2+2) + '\n'
        line = block*2
        for i in range(n2):
            line += dash*(3*n2 + (n2-1)) + block*2
        line += '\n'

        outs = solid_line
        for a in range(n2):
            for b in range(n2):
                for c in range(n2):
                    outs += block*2
                    for d in range(n2):
                        nxt = self.get(n2*c+d, n2*a+b)
                        if d != 0:
                            outs += '|'
                        outs += ' ' + (str(nxt) if nxt is not None else ' ') + ' '
                outs += block*2 + '\n'
                if (b+1) < n2:
                    outs += line
            outs += solid_line
        print outs

    def printp(self):
        n = self._n
        n2 = self._n2
        assert n == 9
        assert n2 == 3

        width = 11
        dash = u'\u2013'
        block = u'\u2588'
        solid_line = block*(12*n+n2+2) + '\n'
        line = block*2
        for i in range(n2):
            line += dash*(11*n2 + (n2-1)) + block*2
        line += '\n'

        def to_disp_on_line(nxt, ln):
            n = len(nxt)
            if n <= 3:
                return nxt if ln == 1 else []
            elif n == 4:
                if ln == 0: return nxt[:2]
                if ln == 2: return nxt[2:]
                return []
            elif n == 5:
                if ln == 0: return nxt[:2]
                if ln == 2: return nxt[3:]
                return [ nxt[2] ]
            elif n == 6:
                return nxt[2*ln:2*(ln+1)]
            elif n == 7:
                if ln == 0: return nxt[:2]
                if ln == 1: return nxt[2:5]
                if ln == 2: return nxt[5:]
            elif n == 8:
                if ln == 0: return nxt[:3]
                if ln == 1: return nxt[3:5]
                if ln == 2: return nxt[5:]
            elif n == 9:
                return nxt[3*ln:3*(ln+1)]

        def format_vls(vls):
            if len(vls) == 0: return ' '*width
            center = ' , '.join([ str(i) for i in vls ])
            padding = ' '*((width - len(center))/2)
            ret = padding + center + padding
            assert len(ret) == width
            return ret

        outs = solid_line
        for y in range(n):
            for ln in range(3):
                outs += block*2
                for x in range(n):
                    nxt = self.pencil(x,y)
                    nxt = nxt if len(nxt) else [ self.get(x,y) ]
                    to_disp = to_disp_on_line(nxt, ln)
                    outs += format_vls(to_disp)
                    outs += '|' if (x % n2) != 2 else block*2
                outs += '\n'
            outs += line if (y % n2) != 2 else solid_line
        print outs
