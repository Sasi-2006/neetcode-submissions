class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))
        queue = deque([(src, 0)])
        dist = [float('inf')] * n
        dist[src] = 0
        stops = 0
        while queue and stops <= k:
            size = len(queue)
            temp = dist.copy()
            for _ in range(size):
                node, cost = queue.popleft()
                for nei, price in graph[node]:
                    if cost + price < temp[nei]:
                        temp[nei] = cost + price
                        queue.append((nei, cost + price))
            dist = temp
            stops += 1
        return dist[dst] if dist[dst] != float('inf') else -1