class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return
            for i in range(start, len(nums)):
                if nums[i] > target:
                    break
                path.append(nums[i])
                backtrack(i, target - nums[i], path)
                path.pop()
        backtrack(0, target, [])
        return result