# Simple implementation of a Graph class with Dijkstra's algorithm.
# Based on https://gist.github.com/econchick/4666413
# Hector CORRAL - BJTU 2019

from collections import defaultdict, deque


class Graph(object):
    """
    Graph of nodes linked by edges.
    Edges have a given value representing distance between two nodes.
    Edges can be either directional or non-directional.

    Implementation of dijkstra's algorithm for calculating the distance between two nodes.
    """
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, name):
        """
        Add a node to the graph.

        :param name: Name of the node
        """
        self.nodes.add(name)

    def add_edge(self, from_node, to_node, distance, directional=False):
        """
        Add edge between two nodes of the graph, with a given distance.

        :param from_node: Origin node
        :param to_node: Destination node
        :param distance: Edge distance value
        :param directional: Set to True for a directional edge (optional)
        """
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance
        if not directional:
            self.edges[to_node].append(from_node)
            self.distances[(to_node, from_node)] = distance

    def dijkstra(self, initial):
        """
        Apply dijkstra algorithm from the given node.

        :param initial: Initial node
        :return visited, paths:
        """
        visited = {initial: 0}
        paths = {}

        nodes = set(self.nodes)

        while nodes:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None or visited[node] < visited[min_node]:
                        min_node = node

            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visited[min_node]

            for edge in self.edges[min_node]:
                try:
                    weight = current_weight + self.distances[(min_node, edge)]
                except KeyError:
                    continue
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    paths[edge] = min_node

        return visited, paths

    def full_path(self, origin, dest):
        """
        Returns shortest distance and path from origin to dest.

        :param origin: Origin node
        :param dest: Destination node
        :return distance, path:
        """
        visited, paths = self.dijkstra(origin)
        full_path = deque()
        try:
            _dest = paths[dest]
        except KeyError:
            raise KeyError('No existing path from {} to {}. The two nodes are not connected.'.format(origin, dest))

        while _dest != origin:
            full_path.appendleft(_dest)
            _dest = paths[_dest]

        full_path.appendleft(origin)
        full_path.append(dest)

        return visited[dest], list(full_path)


if __name__ == '__main__':
    romania = Graph()

    for city in [
        'Arad',
        'Zerind',
        'Oradea',
        'Sibiu',
        'Fagaras',
        'Bucharest',
        'Pitesti',
        'Rimnicu Vilcea'
    ]:
        romania.add_node(city)

    romania.add_edge('Arad', 'Zerind', 75)
    romania.add_edge('Arad', 'Sibiu', 140)
    romania.add_edge('Zerind', 'Oradea', 71)
    romania.add_edge('Oradea', 'Sibiu', 151)
    romania.add_edge('Sibiu', 'Fagaras', 99)
    romania.add_edge('Sibiu', 'Rimnicu Vilcea', 80)
    romania.add_edge('Fagaras', 'Bucharest', 211)
    romania.add_edge('Bucharest', 'Pitesti', 101)
    romania.add_edge('Pitesti', 'Rimnicu Vilcea', 97)

    distance, path = romania.full_path('Arad', 'Bucharest')
    path = ' -> '.join(path)
    print('From Arad to Bucharest, distance: {}km, path: {}'.format(distance, path))
