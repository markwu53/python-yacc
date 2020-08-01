from pbase import *
from plbase import *
from plmanual import *
from plgencode import *

one = P(
    attach_type("identifier", identifier)
    , attach_type("ysymbol", ysymbol)
    , attach_type("space", space)
    , attach_type("line_comment", line_comment)
    , attach_type("block_comment", block_comment)
    , attach_type("symbol", symbol))

def lexer(): return [e for e in flatten(Z(one)(0).r) if e.t not in remove_types]
