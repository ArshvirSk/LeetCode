class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        counts = {}

        for i in range(len(nums)):
            if nums[i] in counts:
                counts[nums[i]] += 1
            else:
                counts[nums[i]] = 1
        
        for i in list(counts.values()):
            if i >= 2:
                return True
        
        return False