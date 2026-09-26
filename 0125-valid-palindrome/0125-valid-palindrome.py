import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        s =  re.sub(r'[^a-zA-Z0-9\s]', '', s)
        reverse_s = s[::-1]
        return reverse_s == s