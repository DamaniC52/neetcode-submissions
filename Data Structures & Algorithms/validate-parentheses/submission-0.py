class Solution:
    def isValid(self, s: str) -> bool:
        
        Hash = {")":"(" , "}":"{" , "]" : "[" }
        stack = []
        for char in s:
            if char in Hash:
                if stack and stack[-1] == Hash[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack