class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(arr):
            prev2 = 0
            prev1 = 0
            for money in arr:
                current = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = current
            return prev1
        n = len(nums)
        if n == 1:
            return nums[0]
        money1 = rob_linear(nums[:-1])
        money2 = rob_linear(nums[1:])
        return max(money1, money2)