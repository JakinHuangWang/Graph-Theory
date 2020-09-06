from collections import defaultdict


class Graph:
    def __init__(self):
        self.neighbors = defaultdict(list)

    def addEdge(self, u, v):
        self.neighbors[u].append(v)


graph = Graph()
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 2)
graph.addEdge(2, 0)
graph.addEdge(2, 3)
graph.addEdge(3, 3)

visited = [False] * len(graph.neighbors)


def DFS(root):
    queue = []
    queue.append(root)
    visited[root] = True

    while len(queue) > 0:
        node = queue.pop(0)
        print(node)
        for n in graph.neighbors[node]:
            if not visited[n]:
                queue.append(n)
                visited[n] = True


DFS(0)
