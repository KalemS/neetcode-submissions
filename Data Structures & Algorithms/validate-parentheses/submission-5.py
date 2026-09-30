class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        lookup = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for c in s:
            if c in lookup:
                if not stack or lookup[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        
        return not stack
            