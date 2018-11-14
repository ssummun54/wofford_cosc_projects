"""
This module contains functions that provide information about graphs
"""

import cosc350

def hops(graph, start_vertex_key):
    """
    Return the minimum number of hops needed to get from a
    vertex to each of the other vertices reachable from that
    vertex.
    :param graph: a Graph instance
    :param start_vertex_key: the key associated with a vertex in graph
    :return: a list of lists, where the sublist at index k contains
             the keys for vertices k hops away from the vertex
             associated with start_vertex_key.
    """

    queue = cosc350.Queue()

    # enqueue start_vertex_key, 0
    queue.enqueue((start_vertex_key, 0))

    # mark start_vertex_key as visited
    visited_list = [start_vertex_key]
    results = [[] for i in range(len(graph.get_vertices()))]

    # while the queue is not empty:
    while not queue.is_empty():
        #     dequeue vk, h       // vertex key and associated hops
        vk, h = queue.dequeue()

    #     record that vk is h hops from start_vertex_key

        results[h].append(vk)

        #     for each of the neighbors nk of vk:
        #nk = graph.get_neighbors(vk)
        for nk in graph.get_neighbors(vk):
            #         if nk has not been marked as visited
            if nk not in visited_list:
                #             enqueue nk, h + 1
                queue.enqueue((nk, h + 1))
    #             mark nk as having been visited
                visited_list.append(nk)


    return results  # STUB
