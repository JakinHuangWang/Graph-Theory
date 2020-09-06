import collections


class Graph:
    def __init__(self):
        self.neighbor = collections.defaultdict(list)

    def addEdge(self, u, v):
        self.neighbor[u].append(v)


graph = Graph()
all_Components = collections.defaultdict(list)
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 2)
graph.addEdge(2, 0)
graph.addEdge(2, 3)
graph.addEdge(3, 3)
graph.addEdge(4, 5)
graph.addEdge(5, 6)
graph.addEdge(6, 4)
graph.addEdge(7, 8)
graph.addEdge(8, 9)
graph.addEdge(9, 7)

N = len(graph.neighbor)


visited = [False] * N


def findComponents():
    global count
    count = 0
    for i in range(N):
        if not visited[i]:
            print(i)
            DFS(i)
            count += 1


def DFS(root):
    if not visited[root]:
        visited[root] = True
        all_Components[count].append(root)
        for v in graph.neighbor[root]:
            DFS(v)


findComponents()
print(all_Components)
