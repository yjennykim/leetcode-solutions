class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        store = {0:1}
        running = 0

        for num in nums:
            running += num
            prefix = running - k
            if prefix in store:
                total += store[prefix]
            store[running] = store.get(running, 0) + 1

        return total