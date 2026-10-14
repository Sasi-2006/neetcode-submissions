from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)   
        memo = {}                
        def dfs(substring):
            if substring in memo:
                return memo[substring]
            if not substring:
                return [""]
            result = []
            for word in wordSet:
                if substring.startswith(word):
                    remaining_sentences = dfs(substring[len(word):])
                    for sentence in remaining_sentences:
                        if sentence:
                            result.append(word + " " + sentence)
                        else:
                            result.append(word)
            memo[substring] = result
            return result
        return dfs(s)