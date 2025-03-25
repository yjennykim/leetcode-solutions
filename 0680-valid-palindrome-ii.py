class Solution:
    def validPalindrome(self, s: str) -> bool:
        # try deleting the left character first
        l,r = 0, len(s)-1
        deletedOnce = False
        needsDeleteRight = False
        while l <= r:
            if s[l].lower() != s[r].lower():
                if deletedOnce: # if already used deletion, break
                    needsDeleteRight = True
                    break
                l += 1 # ignore left character
                deletedOnce = True
            else:
                l += 1
                r -= 1

        # if deleting left character results in valid palindrome, return True
        if not needsDeleteRight:
            return True
            
        # try deleting the right character next
        l,r = 0 , len(s)-1
        deletedOnce = False
        while l <= r:
            if s[l].lower() != s[r].lower():
                if deletedOnce: # if already used deletion, return False
                    return False
                r -= 1
                deletedOnce = True
            else:
                l += 1
                r -= 1
            
        return True

        
        

            