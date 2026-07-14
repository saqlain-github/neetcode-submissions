class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for x in nums:
            if x not in nums_dict.keys():
                nums_dict[x] = 1
            else:
                return True

        return False
        