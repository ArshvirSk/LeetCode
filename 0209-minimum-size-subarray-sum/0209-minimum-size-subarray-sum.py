class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currsum = 0
        left = 0
        min_len = float("inf")
        
        for i in range(len(nums)):
            currsum += nums[i]

            while currsum >= target:
                min_len = min(min_len, i - left + 1)
                currsum -= nums[left]
                left+=1

        return 0 if min_len == float("inf") else min_len