from strategy import Strategy

class TwoLine(Strategy):
    def apply(self):
        b = self._board
        n2 = b.square_size()
        n = b.size()
        changed = False
        def remove_pencil(col, row, v):
            if b.immutable(col, row): return
            p = b.pencil(col, row)
            if v not in p: return
            p.remove(v)
            changed = True
        # For each cell
        for x in range(n):
            for y in range(n):
                p = b.pencil(x,y)
                if len(p) != 2: continue
                xs = x/n2
                ys = y/n2
                def c(a, b):
                    return a + b*n2
                vals = [ [ b.pencil(c(i,xs),c(k,ys)) for k in range(n2) ] for i in range(n2) ]
                # Look for an equal
                equals = None
                for i in range(n2):
                    for k in range(n2):
                        if c(i, xs) == x and c(k, ys) == y: continue
                        if vals[i][k] == p:
                            assert equals is None
                            equals = [i,k]
                if equals is None:
                    continue
                # For the cell
                for i in range(n2):
                    for k in range(n2):
                        x2 = c(i, xs)
                        y2 = c(k, ys)
                        if x2 == x and y2 == y: continue
                        if i == equals[0] and k == equals[1]: continue
                        remove_pencil(x2, y2, p[0])
                        remove_pencil(x2, y2, p[1])
                # For the column
                ex = c(equals[0], xs)
                ey = c(equals[1], ys)
                if ex == x:
                    for row in range(n):
                        if row == y or row == ey: continue
                        remove_pencil(x, row, p[0])
                        remove_pencil(x, row, p[1])
                # For the row
                if ey == y:
                    for col in range(n):
                        if col == x or col == ex: continue
                        remove_pencil(col, y, p[0])
                        remove_pencil(col, y, p[1])
        return changed
