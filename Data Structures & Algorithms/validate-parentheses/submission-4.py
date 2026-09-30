class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        lookup = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for c in s:
            if c in "}])":
                print(c)
                if not stack or lookup[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0
            