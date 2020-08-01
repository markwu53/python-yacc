from pbase import *
from plbase import *
from plmanual import *

def identifier(p): return postr(passing,S(identifier_first_char,Z(identifier_next_char)))(p)
def identifier_first_char(p): return P(postr(passing,S(is_alpha)),postr(passing,S(C("_"))))(p)
def identifier_next_char(p): return P(postr(passing,S(identifier_first_char)),postr(passing,S(is_digit)))(p)
def space(p): return postr(passing,S(M(is_space)))(p)
def ysymbol(p): return P(postr(passing,S(C("'"),any,C("'"))),postr(passing,S(C('"'),any,C('"'))))(p)
def symbol(p): return postr(passing,S(any))(p)
def line_comment(p): return postr(passing,S(C("/"),C("/"),Z(line_comment_char),line_comment_end))(p)
def block_comment(p): return postr(passing,S(C("/"),C("*"),Z(block_comment_char),C("*"),C("/")))(p)
