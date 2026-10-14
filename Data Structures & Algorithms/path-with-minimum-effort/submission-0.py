class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        heap = [(0, 0, 0)]
        effort = [[float('inf')] * cols for _ in range(rows)]
        effort[0][0] = 0
        while heap:
            curr_effort, r, c = heapq.heappop(heap)
            if r == rows - 1 and c == cols - 1:
                return curr_effort
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    diff = abs(heights[r][c] - heights[nr][nc])
                    new_effort = max(curr_effort, diff)
                    if new_effort < effort[nr][nc]:
                        effort[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))
        return 0