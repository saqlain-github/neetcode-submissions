class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_anagram = {}

        for s in strs:
            sort_s = "".join(sorted(s))
            if sort_s in dict_anagram.keys():
                dict_anagram[sort_s].append(s)
            else:
                dict_anagram[sort_s] = [s]

        return list(dict_anagram.values())
             

        