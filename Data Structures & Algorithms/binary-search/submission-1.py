class Solution:
    def search(self, nums, target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            half = left+((right-left)//2)
        
            if nums[half] == target:
                return half

            if nums[half] < target:
                left = half+1
            elif nums[half] > target:
                right = half-1

        return -1