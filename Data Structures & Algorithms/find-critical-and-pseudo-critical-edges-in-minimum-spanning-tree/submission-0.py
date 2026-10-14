from typing import List
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        self.parent[py] = px
        return True

class Solution:
    def kruskal(self, n, edges, skip_edge=-1, force_edge=None):
        dsu = DSU(n)
        weight = 0
        if force_edge:
            u, v, w, _ = force_edge
            if dsu.union(u, v):
                weight += w
        for i, (u, v, w, idx) in enumerate(edges):
            if i == skip_edge:
                continue
            if dsu.union(u, v):
                weight += w
        root = dsu.find(0)
        for i in range(n):
            if dsu.find(i) != root:
                return float('inf')
        return weight
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [edge + [i] for i, edge in enumerate(edges)]
        edges.sort(key=lambda x: x[2])
        base_weight = self.kruskal(n, edges)
        critical = []
        pseudo = []
        for i in range(len(edges)):
            if self.kruskal(n, edges, skip_edge=i) > base_weight:
                critical.append(edges[i][3])
            elif self.kruskal(n, edges, force_edge=edges[i]) == base_weight:
                pseudo.append(edges[i][3])
        return [critical, pseudo]