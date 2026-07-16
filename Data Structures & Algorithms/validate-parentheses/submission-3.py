class Solution:
    def isValid(self, s: str) -> bool:
        root_dict = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        stack = []
        i = 0
        while i < len(s):
            print(stack, s[i])
            if s[i] in root_dict.values():
                stack.append(s[i])
            elif s[i] in root_dict.keys():
                if len(stack) == 0 or stack[-1] != root_dict[s[i]]:
                    return False
                elif stack[-1] == root_dict[s[i]]:
                    stack.pop()
            i += 1

        return not stack