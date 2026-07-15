class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res_Dict = {}

        for i, x in enumerate(nums):
            res_Dict[x] = res_Dict.get(x, 0) + 1

        return sorted(res_Dict, key=res_Dict.get)[-k:]