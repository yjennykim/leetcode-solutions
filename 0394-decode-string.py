class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                # Step 1: Get the string inside the brackets
                substr = ''
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()  # Remove the '['

                # Step 2: Get the number before the brackets
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                # Step 3: Repeat the substring and push back to stack
                stack.append(int(num) * substr)

        return ''.join(stack)
