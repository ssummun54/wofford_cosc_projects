"""
This program computes the hops needed to get from a given
vertex in a graph to every other vertex. It takes two
command line arguments:
    file name: the name of a file containing a graph
    vertex key: a key from a vertex in the graph

The graph file is a text file in which each line
gives a vertex key followed by keys for its neighbors.
A vertex key is any sequence of non-whitespace
characters.
"""

import sys
import graphs
import graphinfo


def main():
    """
    Determine the vertices that can be reached in 1 hop,
    2 hops, and so on from a specific vertex and then
    display that information.
    :return: None
    """

    # Get the command line arguments
    if len(sys.argv) != 3:
        print('Usage: {} file-name vertex-key'.format(sys.argv[0]), file=sys.stderr)

    graph_filename, start_vertex_key = sys.argv[1], sys.argv[2]

    try:
        with open(graph_filename, 'r') as graph_file:

            # Construct an empty graph
            graph = graphs.Graph()

            # Process the file data
            for line in graph_file:
                vertex_keys = line.split()
                if vertex_keys:
                    k, neighbor_keys = vertex_keys[0], vertex_keys[1:]
                    for neighbor_key in neighbor_keys:
                        graph.add_edge(k, neighbor_key)

            print("Graph to be processed:")
            for key in sorted(graph.get_vertices()):
                print('{:>5}: {}'.format(key, ' '.join(sorted(graph.get_neighbors(key)))))

        # Determine the number of hops and then display the result
        hops_list = graphinfo.hops(graph, start_vertex_key)
        print('Hops from {}:'.format(start_vertex_key))
        for i, sublist in enumerate(hops_list):
            if sublist:
                print('{:>5} hops: {}'.format(i, ', '.join(sorted(sublist))))

    except FileNotFoundError:
        print('Could not open file {}.'.format(graph_filename), file=sys.stderr)


if __name__ == '__main__':
    main()
