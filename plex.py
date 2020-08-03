from pbase import *
from plexbase import *
from plexbefore import *

def identifier(p): return S(identifier_first_char,Z(identifier_next_char))(p)
def identifier_first_char(p): return P(is_alpha,C("_"))(p)
def identifier_next_char(p): return P(identifier_first_char,is_digit)(p)
def space(p): return M(is_space)(p)
def ysymbol(p): return S(quote,any,quote)(p)
def ykeyword(p): return S(dquote,identifier,dquote)(p)
def symbol(p): return any(p)
def line_comment(p): return S(C("/"),C("/"),Z(line_comment_char),line_comment_end)(p)
def block_comment(p): return S(C("/"),C("*"),Z(block_comment_char),C("*"),C("/"))(p)
