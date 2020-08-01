from pbase import *
from ppbase import *
from ppmanual import *

def y_grammar(p): return postr(passing,S(M(y_entry)))(p)
def y_entry(p): return postr(pdef,S(y_term,s("="),y_entry_def,s(";")))(p)
def y_entry_def(p): return postr(pcombine,S(y_sequence,y_or_sequences))(p)
def y_or_sequences(p): return postr(pcollect,S(Z(y_or_sequence)))(p)
def y_or_sequence(p): return postr(pskip,S(s("|"),y_sequence))(p)
def y_sequence(p): return postr(ppost,S(y_seq_objects,O(y_post_processing)))(p)
def y_post_processing(p): return postr(pskip,S(p_post_op,y_processing))(p)
def p_post_op(p): return postr(passing,S(s("-"),s(">")))(p)
def y_seq_objects(p): return postr(pseq,S(M(y_seq_object)))(p)
def y_seq_object(p): return P(postr(pzero,S(y_term,s("*"))),postr(pmore,S(y_term,s("+"))),postr(poptional,S(y_term,s("?"))),postr(passing,S(y_term)),postr(passing,S(y_symbol)))(p)
def y_term(p): return postr(passing,S(y_identifier))(p)
def y_processing(p): return postr(passing,S(y_identifier))(p)
