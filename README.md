# Tree and Graph Analyzer

This project provides a collection of algorithms for analyzing tree and graph properties using Python.

## Features
- **Tree validation:** Check if a graph is a tree or forest.
- **Tree properties:** Compute diameter, radius, and centers of a tree.
- **Graph traversal:** BFS and DFS implementations.

## Code Example

Here’s an example of how to use the functions:

```python
from graph_tree_analysis import tree_attributes, is_tree

# Example adjacency matrix
adj_matrix = [
    [0, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 0]
]

if is_tree(adj_matrix):
    print(tree_attributes(adj_matrix))  # Output: [centers, radius, diameter]
else:
    print("This graph is not a tree.")
