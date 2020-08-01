from pbase import *
from ppbase import *
import pdata
import ppdata

p1 = lambda r: [r[0].v]
#ps1 = lambda r: ['s("{}")'.format(r[0].v)]
def ps1(r):
    ch = r[0].v[1:-1]
    if pdata.phase == "yacc":
        ret = "s('{}')".format(ch) if ch == '"' else 's("{}")'.format(ch)
        return [ret]
    ret = "C('{}')".format(ch) if ch == '"' else 'C("{}")'.format(ch)
    return [ret]
ps2 = lambda r: ['kword("{}")'.format(r[0].v)]
pzero = lambda r: ["Z({})".format(flatten(r)[0])]
pmore = lambda r: ["M({})".format(flatten(r)[0])]
poptional = lambda r: ["O({})".format(flatten(r)[0])]
pseq = lambda r: ["S({})".format(",".join(flatten(r)))]
def ppost(r):
    x = flatten(r)
    if len(x) == 2:
        ret = "postr({1},{0})".format(*x)
    else:
        ret = "postr(passing,{})".format(*x)
    return [ret]
pskip = lambda r: [r[1]]
pcollect = lambda r: flatten(r)
pcombine = lambda r: [(lambda x: x[0] if len(x) == 1 else "P({})".format(",".join(x)))(r[0]+r[1])]
pdef = lambda r: ["def {0}(p): return {2}(p)".format(*flatten(r))]
def pdef(r):
    ppdata.defined_terms.add(flatten(r)[0])
    return ["def {0}(p): return {2}(p)".format(*flatten(r))]

y_symbol = postr(ps1, ttype("ysymbol"))
y_keyword = postr(ps2, ttype("keyword"))
y_processing = postr(p1, ttype("identifier"))
y_identifier = postr(p1, ttype("identifier"))
