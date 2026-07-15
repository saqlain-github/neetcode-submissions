class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sorted_S = ''.join(sorted(s))
            res[sorted_S].append(s)

        return list(res.values())