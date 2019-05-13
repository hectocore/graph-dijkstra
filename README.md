# graph-dijkstra
Simple implementation of a Graph class with Dijkstra's algorithm.

## Usage

### As a python library
Simply import the `Graph` model from `dijkstra` library.

Implementation example:
```python
from dijkstra import Graph

graph = Graph()

for node in ['A', 'B', 'C', 'D', 'E']:
    graph.add_node(node)

graph.add_edge('A', 'B', 10)
graph.add_edge('B', 'C', 30)
graph.add_edge('C', 'D', 20)
graph.add_edge('D', 'E', 15)
graph.add_edge('E', 'B', 32)

distance, path = graph.full_path('A', 'E')
path = ' -> '.join(path)
print('From A to E, distance: {}, path: {}'.format(distance, path))
# From A to E, distance: 42, path: A -> B -> E
```

### As a program - for testing
Simply run `python dijkstra` (must be python 3)

You should see the following output:
```sh
python dijkstra.py
    From Arad to Bucharest, distance: 418km, path: Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest
```
