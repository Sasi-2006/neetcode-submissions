class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        reach = [[False] * numCourses for _ in range(numCourses)]
        for a, b in prerequisites:
            reach[a][b] = True
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if reach[i][k] and reach[k][j]:
                        reach[i][j] = True
        result = []
        for u, v in queries:
            result.append(reach[u][v])
        return result