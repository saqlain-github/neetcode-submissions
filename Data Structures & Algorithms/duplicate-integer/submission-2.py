"""class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for x in nums:
            if x not in nums_dict.keys():
                nums_dict[x] = 1
            else:
                return True

        return False"""

"""class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False"""


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))
        