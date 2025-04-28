class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures) 
        st = []  # previous days that need to be processed - monotonically decreasing stack

        for i,temp in enumerate(temperatures):
            while st and temp > st[-1][-1]:
                j, small_temp = st.pop()
                days[j] = i-j  # update all previous days which are colder

            st.append((i,temp))
        
        return days
