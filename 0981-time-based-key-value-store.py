class TimeMap:

    def __init__(self):
        self.cache = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = []
        
        self.cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values_list = self.cache.get(key, [])
        # Largest possible timestamp <= timestamp

        l,r = 0, len(values_list) - 1
        while l <= r:
            m = (l + r) // 2
            if values_list[m][0] <= timestamp:
                # too small
                l = m + 1
            elif values_list[m][0] > timestamp:
                # too big
                r = m - 1
    
        if r >= 0:
            return values_list[r][1]
        
        return ""



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)