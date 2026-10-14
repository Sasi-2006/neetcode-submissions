class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26
        if len(s) != len(t):
            return False
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        for ch in t:
            count[ord(ch)- ord('a')] -= 1
        return all(c == 0 for c in count)