class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target = len(nums)

        for i in range(len(nums)):
            target += i - nums[i]

        return target