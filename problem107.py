"""
Minimal network

The following undirected network consists     |    The same network can be
of seven vertices and twelve edges with       |    represented by the matrix below:
a total weight of 243:                        |
                                              |         A   B   C   D   E   F   G
          20                                  |    A    -   16  12  21  -   -   -
      B---------E                             |    B    16  -   -   17  20  -   -
     / \       / \                            |    C    12  -   -   28  -   31  -
  16/ 17\   18/   \11                         |    D    21  17  28  -   18  19  23
   /     \   /     \                          |    E    -   20  -   18  -   -   11
  /   21  \ /   23  \                         |    F    -   -   31  19  -   -   27
 A---------D---------G                        |    G    -   -   -   23  11  27  -
  \       / \       /                         |
   \   28/   \   27/                          |
  12\   /   19\   /                           |
     \ /       \ /                            |
      C---------F                             |
          31

However, it is possible to optimize the network by removing some edges and still ensure that all points on the network
remain connected. The network which achieves the maximum saving is shown below. It has a weight of 93, representing a
saving of 243 - 93 = 150 from the original network.


      B         E
     / \       / \
  16/   \   18/   \
   /   17\   /   11\
  /       \ /       \
 A         D         G
  \         \
   \         \
  12\       19\
     \         \
      C         F

Using network.txt (right click and 'Save Link/Target As...'), a 6K text file containing a network with forty vertices,
and given in matrix form, find the maximum saving which can be achieved by removing redundant edges whilst ensuring that
the network remains connected.
"""

# i.e., find the minimum spanning tree
from time import time


def graph_weight(graph):
    return sum(graph.values())


def subgraphs(graph):
    subs = []
    while graph:
        sub = _get_subgraph(graph)
        subs.append(sub)
        graph = {k: v for k, v in graph.items() if k not in sub}
    return subs


def _get_subgraph(graph):
    """Get an arbitrary subgraph"""
    edges = set(graph.keys())
    nodes = {node for edge in edges for node in edge}
    starting_edge = edges.pop()
    found_nodes = set(starting_edge)
    found_edges = {starting_edge}
    connected_edges = True
    while connected_edges:
        connected_edges = {edge for edge in edges if any(node in found_nodes for node in edge)}
        connected_nodes = {node for edge in connected_edges for node in edge}
        found_edges.update(connected_edges)
        found_nodes.update(connected_nodes)
        edges -= connected_edges
    return {edge: graph[edge] for edge in found_edges}


def find_mst(graph):
    # For any cut in an edge-weighted graph, the crossing edge of minimum weight is in the MST. The edges surrounding
    # any given node form a cut, so use that to find a list of starting edges.
    nodes = {node for edge in graph for node in edge}
    mst = {}
    for node in nodes:
        connected_edges = {edge for edge in graph if node in edge}
        best_edge = min(connected_edges, key=lambda edge: graph[edge])
        mst[best_edge] = graph[best_edge]
    # Now we probably have a disconnected graph. Get the subgraphs and apply the same notion; pick a subgraph, and
    # choose the edge that connects it to any other subgraph as being part of the MST. Then reevaluate until there is
    # only one graph.
    parts = subgraphs(mst)
    while len(parts) > 1:
        subgraph = parts.pop()
        subgraph_nodes = {node for edge in subgraph for node in edge}
        connected_edges = {edge for edge in graph if sum(node in subgraph_nodes for node in edge) == 1}
        best_edge = min(connected_edges, key=lambda edge: graph[edge])
        mst[best_edge] = graph[best_edge]
        parts = subgraphs(mst)
    return mst


A, B, C, D, E, F, G = range(7)
sample_network = {
    (A, B): 16, (A, C): 12, (A, D): 21, (B, D): 17,
    (B, E): 20, (C, D): 28, (C, F): 31, (D, E): 18,
    (D, F): 19, (D, G): 23, (E, G): 11, (F, G): 27
}
assert graph_weight(sample_network) - graph_weight(find_mst(sample_network)) == 150

if __name__ == '__main__':
    start = time()
    network = {}
    with open('p107_network.txt') as f:
        for i, line in enumerate(f):
            for j, weight in enumerate(line.rstrip().split(',')):
                try:
                    network[tuple(sorted([i, j]))] = int(weight)
                except ValueError:
                    pass

    original_weight = graph_weight(network)
    mst_weight = graph_weight(find_mst(network))
    print('Answer:', original_weight - mst_weight)
    print(time() - start)
