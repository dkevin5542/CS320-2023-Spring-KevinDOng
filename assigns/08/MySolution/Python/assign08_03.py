####################################################
#!/usr/bin/env python3
####################################################
import queue
"""
HX-2023-04-07: 20 points
The following implementation is stream-based:
# def graph_bfs(nxs, fnexts):
#     visited = set()
#     def helper(qnxs):
#         if qnxs.empty():
#             return strcon_nil()
#         else:
#             nx1 = qnxs.get()
#             # print("gtree_bfs: helper: nx1 = ", nx1)
#             for nx2 in fnexts(nx1):
#                 if not nx2 in visited:
#                     qnxs.put(nx2)
#                     visited.add(nx2)
#             return strcon_cons(nx1, lambda: helper(qnxs))
#         # end-of-(if(qnxs.empty())-then-else)
#     qnxs = queue.Queue()
#     for nx0 in nxs:
#         qnxs.put(nx0)
#         visited.add(nx1)
#     return lambda: helper(qnxs)
Please give a generator-based implementation of graph_bfs!!!
"""
def generator_graph_bfs(nxs, fnexts):
    """
    This function does the same as graph_bfs.
    """
    mark = set()
    hold = queue.Queue()

    for i in nxs:
        hold.put(i)
        mark.add(i)

    while not hold.empty():
        take = hold.get()
        yield take
        for nx2 in fnexts(take):
            if nx2 not in mark:
                hold.put(nx2)
                mark.add(nx2)
####################################################
