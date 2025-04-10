class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []
        for ch in s:
            # opening paren
            if ch in matches:
                # add corresponding closing paren to stack
                stack.append(matches[ch])
            else:
                if len(stack) == 0:
                    return False
                
                if stack.pop() != ch:
                    return False
        
        return len(stack) == 0