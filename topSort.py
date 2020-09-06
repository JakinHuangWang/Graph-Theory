from collections import defaultdict


class Graph:
    def __init__(self):
        self.neighbors = defaultdict(list)

    def addEdge(self, u, v):
        self.neighbors[u].append(v)


g = Graph()
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

N = 6
visited = [False] * N
stack = []


def topSort():
    for i in range(N):
        if not visited[i]:
            dfs(i)
    print(stack)


def dfs(root):
    if not visited[root]:
        visited[root] = True
        for n in g.neighbors[root]:
            dfs(n)
        stack.insert(0, root)


topSort()
