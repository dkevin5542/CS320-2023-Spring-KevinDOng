####################################################
#!/usr/bin/env python3
####################################################
import sys
####################################################
sys.path.append('../../../07')
sys.path.append('./../../../../mypylib')
####################################################
from dictwords import *
from mypylib_cls import *
from assign05_02 import *
####################################################
"""
HX-2023-03-24: 10 points
Solving the doublet puzzle
"""
####################################################
"""
Please revisit assign06_04.py.
######
Given a word w1 and another word w2, w1 and w2 are a
1-step doublet if w1 and w2 differ at exactly one position.
For instance, 'water' and 'later' are a 1-step doublet.
The doublet relation is the reflexive and transitive closure
of the 1-step doublet relation. In other words, w1 and w2 are
a doublet if w1 and w2 are the first and last of a sequence of
words where every two consecutive words form a 1-step doublet.
<Here is a little website where you can use to check if two words
for a doublet or not:
http://ats-lang.github.io/EXAMPLE/BUCS320/Doublets/Doublets.html
######
"""
####################################################
def doublet_bfs_test(w1, w2):
    """
    Given two words w1 and w2, this function should
    return None if w1 and w2 do not for a doublet. Otherwise
    it returns a path connecting w1 and w2 that attests to the
    two words forming a doublet.
    """
    def child(node):
        #  takes a word node as input and returns a list of its neighbors
        n = word_neighbors(node)
        return foreach_to_filter_fnlist(fnlist_foreach)(n, lambda word: word_is_legal(word))

    helper = stream_make_filter(gpath_bfs([w1], child), lambda path: path[-1] == w2)()
    if helper.get_ctag() == 0:
        # empty if no path was found
        return None
    else:
        # returns the first element of the stream, which is the shortest path between w1 and w2.
        return helper.get_cons1()
####################################################
