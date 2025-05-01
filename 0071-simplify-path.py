class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        path_list = path.split("/")
        
        for word in path_list:
            if word == "." or word == "":
                continue
            elif word == "..":
                if stack:
                    stack.pop()  # only replace words that are double period
            else:
                stack.append(word)         

        return '/' + '/'.join(stack)
            
            