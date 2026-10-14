class Solution:
    def topoSort(self, k, conditions):
        graph = defaultdict(list)
        indegree = [0] * (k + 1)
        for u, v in conditions:
            graph[u].append(v)
            indegree[v] += 1
        q = deque()
        for i in range(1, k + 1):
            if indegree[i] == 0:
                q.append(i)
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        if len(order) != k:
            return []
        return order
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rowOrder = self.topoSort(k, rowConditions)
        colOrder = self.topoSort(k, colConditions)
        if not rowOrder or not colOrder:
            return []
        rowPos = {num: i for i, num in enumerate(rowOrder)}
        colPos = {num: i for i, num in enumerate(colOrder)}
        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            r = rowPos[num]
            c = colPos[num]
            matrix[r][c] = num
        return matrix