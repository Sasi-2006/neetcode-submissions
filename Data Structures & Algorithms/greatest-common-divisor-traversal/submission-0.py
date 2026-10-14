class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        if 1 in nums:
            return False
        parent = list(range(n))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
        factor_map = {}
        for i, num in enumerate(nums):
            x = num
            d = 2
            while d * d <= x:
                if x % d == 0:
                    if d in factor_map:
                        union(i, factor_map[d])
                    else:
                        factor_map[d] = i

                    while x % d == 0:
                        x //= d
                d += 1
            if x > 1:
                if x in factor_map:
                    union(i, factor_map[x])
                else:
                    factor_map[x] = i
        root = find(0)
        for i in range(1, n):
            if find(i) != root:
                return False
        return True