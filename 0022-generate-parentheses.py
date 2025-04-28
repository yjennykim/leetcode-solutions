class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def generate(num_opening, num_closing, curr):
            if num_opening + num_closing == n*2:
                res.append(curr)
                return
            
            if num_opening < n:
                generate(num_opening + 1, num_closing, curr + "(")
            
            if num_opening > num_closing:
                generate(num_opening, num_closing+1, curr+")")
        
        generate(0,0,"")
        return res
            