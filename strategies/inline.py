from strategy import Strategy
from utilities import merge

class InLine(Strategy):
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
        # For each square
        for xs in range(n2):
            for ys in range(n2):
                def c(a, b):
                    return a + b*n2
                vals = [ [ b.pencil(c(i,xs),c(k,ys)) for k in range(n2) ] for i in range(n2) ]
                # For each value
                for vl in b.range():
                    # For each column
                    for col in range(n2):
                        # Make sure vl is in column col but no other cell
                        if vl not in merge(*vals[col]): continue
                        vls2 = [ i for idx,i in enumerate(vals) if idx != col ]
                        if vl in merge(*merge(*vls2)): continue
                        # Remove vl from everything else in the column
                        for row in range(n):
                            if row >= c(0, ys) and row < c(0, ys+1):
                                continue
                            remove_pencil(c(col, xs), row, vl)
                    # For each row
                    for row in range(n2):
                        # Make sure vl is in column col but no other cell
                        this_row = [ vals[i][row] for i in range(n2) ]
                        if vl not in merge(*this_row): continue
                        vls2 = [ i[k] for k in range(n2) if k != row for i in vals ]
                        if vl in merge(*vls2): continue
                        # Remove vl from everything else in the row
                        for col in range(n):
                            if col >= c(0, xs) and col < c(0, xs+1):
                                continue
                            remove_pencil(col, c(row, ys), vl)
        return changed
