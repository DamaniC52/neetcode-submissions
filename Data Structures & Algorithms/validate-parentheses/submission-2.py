class Solution:
    def isValid(self, s: str) -> bool:
        hash = {")": "(", "}": "{", "]": "["}

        stack = []

        for char in s:
            if char in hash:
                if stack and stack[-1] == hash[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack