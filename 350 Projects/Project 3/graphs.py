class Graph:
    """
    A graph is a set of vertices and edges.
    """

    class _Vertex:
        """
        A vertex in a graph. A vertex is associated with a key
        and keeps track of its neighbors.
        """
        def __init__(self, key):
            """
            Initialize a vertex associated with a given key
            :param key: a number or a str value
            """
            self._key = key
            self._neighbors = set()

        def add_neighbor(self, neighbor_key):
            """
            Add a neighbor to this vertex
            :param neighbor_key: the key for the neighbor vertex
            :return: None
            """
            self._neighbors.add(neighbor_key)

        def get_neighbors(self):
            """
            Get the keys of all the neighbors
            :return: an iterator over the keys for neighbor vertices
            """
            return iter(self._neighbors)

        def get_key(self):
            """
            Get the key associated with this vertex
            :return: the key associated with this vertex
            """
            return self._key

        def __str__(self):
            return "[{}]".format(self._key)

    def __init__(self):
        """
        Initialize a graph to be empty
        """
        self._vertices = {}

    def add_vertex(self, key):
        """
        Add a vertex to this graph
        :param key: a vertex key (hashable value)
        :return: None
        """
        self._vertices[key] = Graph._Vertex(key)

    def get_neighbors(self, key):
        """
        Return a sequence of the neighbors of the vertex associated
        with a vertex
        :param key: the key associated with a vertex in this graph
        :return: a sequence of keys for the neighbors of the vertex
                 associated with key
        """
        return [vertex.get_key() for vertex in self._get_vertex(key).get_neighbors()]

    def add_edge(self, from_key, to_key):
        """
        Add an edge to this graph. If a vertex is not associated
        with either key, then add a vertex to be associated with it
        :param from_key: the id associated with a vertex
        :param to_key: the id associated with another vertex
        :return: None.
        """
        # Create a vertex (or two) if not yet in the graph
        if from_key not in self._vertices:
            self.add_vertex(from_key)
        if to_key not in self._vertices:
            self.add_vertex(to_key)

        # Add a neighbor for each vertex (if not already there)
        if to_key not in self.get_neighbors(to_key):
            self._vertices[from_key].add_neighbor(self._vertices[to_key])
            self._vertices[to_key].add_neighbor(self._vertices[from_key])

    def get_vertices(self):
        """
        Return a list of keys associated with all vertices
        :return: a list of the vertex keys in this graph
        """
        return list(self._vertices.keys())

    def __iter__(self):
        """
        Return an iterator over the vertex keys in this graph
        :return: an iterator
        """
        return iter(self._vertices.keys())

    def __contains__(self, n):
        """
        Determine whether a vertex is associated with key n in this graph
        :param n: a key value
        :return: True if a vertex is associated with key n,
                 False otherwise
        """
        return n in self._vertices

    def __len__(self):
        """
        Return the number of vertices in this graph
        :return: the number of vertices
        """
        return len(self._vertices)

    def _get_vertex(self, n):
        """
        Return the vertex associated with a key
        :param n: a key value
        :return: the vertex object associated with key n
                 or None if no vertex is associated with n
        """
        return self._vertices.get(n, None)


if __name__ == '__main__':
    g = Graph()

    for key in range(6):
        g.add_vertex(key)

    print('Vertices:', ', '.join([str(key) for key in g.get_vertices()]))

    g.add_edge(0, 1)
    g.add_edge(0, 5)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 0)
    g.add_edge(5, 4)
    g.add_edge(5, 2)

    for vertex_key in g:
        print("Vertex", vertex_key)
        for neighbor in g.get_neighbors(vertex_key):
            print("(%s, %s)" % (vertex_key, neighbor))
