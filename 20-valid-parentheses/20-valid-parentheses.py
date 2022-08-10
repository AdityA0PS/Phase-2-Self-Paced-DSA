class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')' : '(', '}' : '{', ']' : '['}
        inputs = ['(', '{', '[']
        stack = []
        
        for char in s:
            if char in inputs:
                stack.append(char)
            else:
                check = pairs[char]
                if len(stack) == 0 or check != stack[-1]:
                    return False
                else:
                    stack.pop()
        
        if len(stack) == 0:        
            return True
        return False