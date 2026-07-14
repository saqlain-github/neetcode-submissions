class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        total_subsets = 1<<n
        final_subset = []

        for i in range(total_subsets):
            current_subset = []

            for j in range(n):
                if i & (1 << j) != 0:
                    current_subset.append(nums[j])

            final_subset.append(current_subset)

        return final_subset


        