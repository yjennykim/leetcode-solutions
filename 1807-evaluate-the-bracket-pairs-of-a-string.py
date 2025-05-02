class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        lookup = {}
        for key,value in knowledge:
            lookup[key] = value
        
        stack = []
        for ch in s:
            if ch != ")":
                stack.append(ch)
            else:
                key = ""
                while stack and stack[-1] != "(":
                    key = stack.pop() + key

                stack.pop() # remove [ 
                if key in lookup:
                    stack.append(lookup[key])
                else:
                    stack.append("?")

        return ''.join(stack)
            