class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        indegree = {c: 0 for word in words for c in word}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indegree[c2] += 1
                    break
        queue = deque([c for c in indegree if indegree[c] == 0])
        result = []
        while queue:
            char = queue.popleft()
            result.append(char)
            for nei in adj[char]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        if len(result) < len(indegree):
            return ""
        return "".join(result)