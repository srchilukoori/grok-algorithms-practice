"""
shortest distance from start to finish using Breadth First Search

        A -------------- Finish
      /   \                |
     /     \               |
start       C              |
     \     /               |
      \   /                |
        B ---------------- D
"""

from collections import deque
from typing import List, Dict, Any


def short_path(start_node: str, graph: Dict[str, Any], end_node: str):
    """shortest path"""
    _queue = deque()
    _queue.append(start_node)
    visited_nodes = set()
    traversed = 0
    while _queue:
        curr_node = _queue.popleft()
        visited_nodes.add(curr_node)
        next_nodes = graph.get(curr_node)
        traversed += 1
        for node in next_nodes:
            if node != end_node:
                _queue.append(node)
            else:
                return traversed


graph = {}
graph["start"] = ["A", "B"]
graph["A"] = ["C", "Finish"]
graph["B"] = ["C", "D"]
graph["D"] = ["Finish"]

assert short_path("start", graph, "Finish") == 2

graph = {}
graph["cab"] = ["cat", "car"]
graph["car"] = ["cat", "bar"]
graph["cat"] = ["mat", "bat"]
graph["bar"] = ["bat"]
graph["mat"] = ["bat"]

assert short_path("cab", graph, "bat") == 2
