class Solution:
    def calPoints(self, operations: List[str]) -> int:
        nums_stack = []

        for op in operations:
            if op == 'D':
                nums_stack.append( nums_stack[-1] * 2 )
            elif op == 'C':
                nums_stack.pop()
            elif op == '+':
                nums_stack.append( nums_stack[-1] + nums_stack[-2] )
            else:
                nums_stack.append(int(op))
        
        return sum(nums_stack)