"""
Using Dijkstra's algorithm find the shortest weighted path
"""
import heapq
from collections import defaultdict


def shortest_weighted_path(paths, start_vertex, end_vertex):
    """
    find the cost of shortest weighted path
    """
    graph = defaultdict(list)
    for src, dest, cost in paths:
        graph[src].append((cost, dest))

    _queue, seen, min_cost_dict = [(0, start_vertex, ())], set(), {start_vertex: 0}

    while _queue:
        curr_cost, src_vertex, path = heapq.heappop(_queue)

        if src_vertex not in seen:
            seen.add(src_vertex)
            path = (src_vertex, path)

            if src_vertex == end_vertex:
                return curr_cost, path

            for min_cost, vertex2 in graph.get(src_vertex, ()):
                if vertex2 not in seen:
                    prev = min_cost_dict.get(vertex2, None)
                    next = curr_cost + min_cost
                    if prev is None or next < prev:
                        min_cost_dict[vertex2] = next
                        heapq.heappush(_queue, (next, vertex2, path))

    return float("inf"), None


if __name__ == "__main__":
    """
        B ----- D
      / | \     | \
    A   |   \   |   F
      \ |     \ | /
        C ----- E
    """

    edges = [
        ("A", "B", 5),
        ("A", "C", 2),
        ("C", "B", 8),
        ("B", "D", 4),
        ("B", "E", 2),
        ("C", "E", 7),
        ("D", "E", 6),
        ("E", "F", 1),
        ("D", "F", 3),
    ]
    assert shortest_weighted_path(edges, "A", "F")[0] == 8

    edges2 = [("A", "B", 10), ("B", "C", 20), ("C", "D", 30), ("C", "E", 1), ("E", "B", 1)]
    assert shortest_weighted_path(edges2, "A", "D")[0] == 60
