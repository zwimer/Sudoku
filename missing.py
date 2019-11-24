from strategy import Strategy

class Missing(Strategy):
    def apply(self):
        n2 = self._board.square_size()
        n = self._board.size()
        b = self._board
        changed = False
        # For eeach square
        for xs in range(n2):
            for ys in range(n2):
                # For each value
                for vl in range(n):
                    def c(a, b):
                        return a + b*n2
                    cs = [ [ (c(i,xs),c(k,ys)) for i in range(n2) ] for k in range(n2) ]
                    vals = [ [ b.pencil(*cs[i][k]) for i in range(n2) ] for k in range(n2) ]
                    first = None
                    only_one = False
                    # Search each cell
                    for i in range(n2):
                        for k in range(n2):
                            if vl in vals[i][k]:
                                only_one = True if first is None else False
                                if first is None:
                                    first = cs[k][i]
                    if only_one:
                        b.set(first[0], first[1], vl)
                        changed = True
        return changed
