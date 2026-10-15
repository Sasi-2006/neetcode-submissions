from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # d ={}
        # if len(nums) == 1:
        #     return nums
        # for i in nums:
        #     if i not in d:
        #         d[i] = 1
        #     elif i in d:
        #         d[i] += 1
        # res = sorted(d, key = lambda x:d[x], reverse = True)
        # return res[:k]
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)
        result = []
        for count in range(len(buckets) - 1, 0 ,-1):
            for num in buckets[count]:
                result.append(num)
                if len(result) == k:
                    return result