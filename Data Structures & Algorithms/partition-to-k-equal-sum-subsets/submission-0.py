class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False
        subsets = [0] * k
        def backtrack(index):
            if index == len(nums):
                return True
            for i in range(k):
                if subsets[i] + nums[index] <= target:
                    subsets[i] += nums[index]
                    if backtrack(index + 1):
                        return True
                    subsets[i] -= nums[index]
                if subsets[i] == 0:
                    break
            return False
        return backtrack(0)