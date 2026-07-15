class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(sorted(set(nums)))
        max_count = 0
        i = 0
        while i < len(nums):
            j = i+1
            while j < len(nums) and abs(nums[j] - nums[j-1]) == 1:
                j += 1
            
            if max_count < (j-i):
                max_count = (j-i)
            i = j
        return max_count
