class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks or sum(matchsticks) % 4 != 0:
            return False
        side = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > side:
            return False
        sides = [0] * 4
        def backtrack(index):
            if index == len(matchsticks):
                return True
            for i in range(4):
                if sides[i] + matchsticks[index] <= side:
                    sides[i] += matchsticks[index]
                    if backtrack(index + 1):
                        return True
                    sides[i] -= matchsticks[index]
                if sides[i] == 0:
                    break
            return False
        return backtrack(0)