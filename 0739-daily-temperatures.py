class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        Input: temperatures = [73,74,75,71,69,72,76,73]
        days = [0] * len(temperatures)
        st = []

        for i,temp in enumerate(temperatures):
            while st and temp > st[-1][-1]:
                j, small_temp = st.pop()
                days[j] = i-j

            st.append((i,temp))
        
        return days
            
                
            
