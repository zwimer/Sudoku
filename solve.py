import sys
from math import sqrt
from copy import deepcopy
from IPython import embed

# Import game board
from board import Board

# Import strategies
sys.path.append(sys.path[0] + '/strategies/')
from simple import Simple
from missing import Missing
from inline import InLine
from twoline import TwoLine
sys.path.pop()


def init_pencil(board):
    for i in range(board.size()):
        for k in range(board.size()):
            cpy = deepcopy(board.range())
            board.set_pencil(i,k, cpy)

def solve(board):
    strategies = [ Simple, Missing, InLine, TwoLine ]
    strategies = [ i(board) for i in strategies ]
    changed = True
    while(changed):
        changed = False
        for strat in strategies:
            changed |= strat.loop()

def main(_):
    board = Board.load(sys.path[0] + '/board.txt')
    init_pencil(board)
    def step():
        solve(board)
        board.printp()
    step()
    board.save(sys.path[0] + '/improved.txt')
    embed()

if __name__ == '__main__':
    main(*sys.argv)
