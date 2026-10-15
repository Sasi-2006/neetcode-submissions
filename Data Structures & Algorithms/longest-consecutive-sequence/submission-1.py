class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # seq = sorted(set(nums))
        # if not seq:
        #     return 0
        # count = 1
        # longest = 1
        # for i in range(len(seq) - 1):
        #     if seq[i+1] == seq[i] + 1:
        #         count += 1
        #     else: 
        #         count = 0
        #     longest = max(longest, count)
        # return longest
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)
        return longest

