class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
            If asteroid is negative, then it is going left so we should compare to elements in stack
            
        """
        st = []  
        for asteroid in asteroids:
            while st and st[-1] > 0 and asteroid < 0:
                if abs(asteroid) > abs(st[-1]):
                    st.pop()
                elif abs(st[-1]) > abs(asteroid):
                    asteroid = 0
                else:
                    # both get destroyed
                    st.pop()
                    asteroid = 0

            if asteroid != 0:
                st.append(asteroid)
        
        return st
        
