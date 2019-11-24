from strategy import Strategy

class InLine(Strategy):
    def apply(self):
        b = self._board
        n2 = b.square_size()
        n = b.size()
        # Vert
        for x in range(n):
            vals = [ b.pencil(x, y) for y in range(n) ]
            # For groups of size
            lengths = [ len(i) for i in vals ]
            for group_size in range(2, max(lengths)):
                grp = self.find_group(vals, group_size)
                if grp == None:
                    continue

    def find_group(self, vals, size):



