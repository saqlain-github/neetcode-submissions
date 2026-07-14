class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dummy = [i for i in range(0, len(nums)+1)]
        
        nums.extend(dummy)
        print(nums)
        target = nums[0]

        for i in nums[1:]:
            target ^= i
        return target