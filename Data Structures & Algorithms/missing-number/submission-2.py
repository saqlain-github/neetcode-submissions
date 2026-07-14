class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target = len(nums)

        for i, x in enumerate(nums):
            target ^= i
            target ^= x

        return target