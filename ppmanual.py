from pbase import *
from ppbase import *
import pdata
import ppdata

p1 = lambda r: [r[0].v]
pzero = lambda r: ["Z({})".format(flatten(r)[0])]
pmore = lambda r: ["M({})".format(flatten(r)[0])]
poptional = lambda r: ["O({})".format(flatten(r)[0])]
pskip = lambda r: [r[1]]
pcollect = lambda r: flatten(r)

def ps1(r):
    ch = r[0].v[1:-1]
    if pdata.phase == "yacc":
        ret = "s('{}')".format(ch) if ch == '"' else 's("{}")'.format(ch)
        return [ret]
    ret = "C('{}')".format(ch) if ch == '"' else 'C("{}")'.format(ch)
    return [ret]

def pseq(r):
    x = flatten(r)
    if len(x) == 1:
        ret = x[0]
    else:
        ret = "S({})".format(",".join(x))
    return [ret]

def ppost(r):
    x = flatten(r)
    if len(x) == 2:
        ret = "postr({1},{0})".format(*x)
    else:
        ret = "postr(passing,{})".format(*x)
    return [ret]

def pcombine(r):
    x = flatten(r)
    if len(x) == 1:
        ret = x[0]
    else:
        ret = "P({})".format(",".join(x))
    return [ret]

def pdef(r):
    ppdata.defined_terms.add(flatten(r)[0])
    ret ="def {0}(p): return {2}(p)".format(*flatten(r))
    return [ret]

y_symbol = postr(ps1, ttype("ysymbol"))
y_identifier = postr(p1, ttype("identifier"))
