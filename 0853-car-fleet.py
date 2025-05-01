class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort by position in descending order
        cars = sorted(zip(position, speed), reverse=True)
        times = [((target - car[0])/car[1]) for car in cars]

        stack = []
        for current_time in times:
            if not stack:
                stack.append(current_time)
            
            # will this car catch up to the one in front of it?
            # if current car will get to target before or at same time as the car in front, then we will catch up and form a fleet.
            car_in_front_of_me_time = stack[-1]
            if car_in_front_of_me_time < current_time:  
                stack.append(current_time)
        
        return len(stack)