class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c):
            if dp[r][c] != 0:
                return dp[r][c]
            max_length = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    matrix[nr][nc] > matrix[r][c]
                ):
                    length = 1 + dfs(nr, nc)
                    max_length = max(max_length, length)
            dp[r][c] = max_length
            return max_length
        answer = 0
        for r in range(rows):
            for c in range(cols):
                answer = max(answer, dfs(r, c))
        return answer