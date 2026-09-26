class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        i = 0
        j = 0
        max_len = 0

        while i < len(s) and j < len(s):
            if s[j] not in sub:
                sub.add(s[j])
                j += 1
                max_len = max(max_len, j - i)
            else:
                sub.remove(s[i])
                i += 1
        return max_len