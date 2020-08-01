from pbase import *
import pldata
import ppdata
import pdata
from plex import *
from pyacc import *

def gencode(phase):
    pdata.phase = phase
    with open("p{}.txt".format(phase)) as fd: pldata.char_source = fd.read()
    token_source = lexer()
    #for e in token_source: print(e)
    used_terms = {term for t,term in token_source if t == "identifier"}
    ppdata.token_source = token_source
    ppdata.defined_terms = set()
    result = parse()
    for e in flatten(result.r): print(e)
    undefined_terms = sorted(list(used_terms-ppdata.defined_terms))
    for e in undefined_terms: print(e)

if __name__ == "__main__":
    gencode("lex")
    gencode("yacc")
