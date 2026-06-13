class Solution:
    def isValid(self, s: str) -> bool:
        map_of_brackets = {}
        map_of_brackets["["] = "]"
        map_of_brackets["{"] = "}"
        map_of_brackets["("] = ")"

        stack = []
        for c in range(len(s)):
            if s[c] in map_of_brackets:
                stack.append(s[c])
            else:
                if not stack:
                    return False

                last_open_bracket = stack.pop()

                if map_of_brackets[last_open_bracket] != s[c]:
                    return False
        
        return len(stack) == 0
    