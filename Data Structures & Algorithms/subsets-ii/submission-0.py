class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset_count = 1 << len(nums)
        final_subset = []

        for i in range(subset_count):
            current_subset = []
            for j in range(i):
                if i & (1 << j) != 0:
                    current_subset.append(nums[j])

            if sorted(current_subset) not in final_subset:
                final_subset.append(sorted(current_subset))

        return final_subset
            