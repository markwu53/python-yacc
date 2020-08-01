import pldata
from pbase import *

def get_char(p): return get_item(p, pldata.char_source)
def check_char(good): return check_item(good, get_char)
def attach_type(type, f): return postr(lambda r: [T(type, "".join(flatten(r)))], f)
def C(c): return check_char(lambda ch: c==ch)
def N1(f): return N(f, get_char)
def CC(pr): return check_char(lambda c: pr(c))
