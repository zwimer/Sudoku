from copy import deepcopy

def intersect(*args):
    assert len(args) > 1
    ret = deepcopy(args[0])
    for i in args[1:]:
        ret = [ deepcopy(k) for k in ret if k in i ]
    return ret

def trim(v, m):
    return (v/m)*m

def merge(*args):
    assert len(args) > 1
    ret = []
    for i in args:
        ret += deepcopy(i)
    return ret
