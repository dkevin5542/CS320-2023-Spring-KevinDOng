####################################################
#!/usr/bin/env python3
####################################################
import sys
import queue
sys.path.append('./../../../../mypylib')
from mypylib_cls import *
sys.path.append('../../../06')
sys.path.append('./../../../../mypylib')
from dictwords import *
from mypylib_cls import *
####################################################
"""
HX-2023-03-24: 30 points
Solving the doublet puzzle
"""
def word_neighbors(word):
    if not word:
        return fnlist_nil()

    neighbors = None
    for i in range(len(word)):
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c != word[i]:
                new_string = word[:i] + c + word[i+1:]
                if neighbors is None:
                    neighbors = fnlist_cons(new_string, fnlist_nil())
                else:
                    neighbors = fnlist_cons(new_string, neighbors)

    if neighbors is None:
        return fnlist_nil()
    else:
        return neighbors

def test_word_neighbors(word):
    return fnlist_filter_pylist (word_neighbors(word), word_is_legal)

def wpath_neighbors_legal(wpath):
    str1 = wpath[-1]
    words = test_word_neighbors(str1)
    return [wpath + (word2,) for word2 in words]

def gtree_bfs(nxs, fchildren):
    def helper(nxs):
        if nxs.empty():
            return strcon_nil()
        else:
            nx1 = nxs.get()
            for nx2 in fchildren(nx1):
                nxs.put(nx2)
            return strcon_cons(nx1, gtree_bfs(nxs, fchildren))
    return lambda: helper(nxs)

def doublet_stream_from(word):
    """
    Please revisit assign05_02.py.
    ######
    Given a word w1 and another word w2, w1 and w2 are a
    1-step doublet if w1 and w2 differ at exactly one position.
    For instance, 'water' and 'later' are a 1-step doublet.
    The doublet relation is the reflexive and transitive closure
    of the 1-step doublet relation. In other words, w1 and w2 are
    a doublet if w1 and w2 are the first and last of a sequence of
    words where every two consecutive words form a 1-step doublet.
    Here is a little website where you can use to check if two words
    for a doublet or not:
    http://ats-lang.github.io/EXAMPLE/BUCS320/Doublets/Doublets.html
    ######
    Given a word, the function [doublet_stream_from] returns a stream
    enumerating *all* the tuples such that the first element of the tuple
    is the given word and every two consecutive words in the tuple form a
    1-step doublet. The enumeration of tuples should be done so that shorter
    tuples are always enumerated ahead of longer ones.
    ######
    """
    nxs = queue.Queue(); nxs.put((word,))
    return gtree_bfs(nxs, wpath_neighbors_legal)
####################################################
####################################################