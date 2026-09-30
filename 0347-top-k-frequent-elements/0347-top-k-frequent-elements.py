class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = {}
        keys = []

        for i in range(len(nums)):
            if nums[i] in counts:
                counts[nums[i]] += 1
            else:
                counts[nums[i]] = 1
        
        for i in range(k):
            max_key = max(counts, key=counts.get)
            keys.append(max_key)
            del counts[max_key]
        
        return keys