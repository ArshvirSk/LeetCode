class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stab = {}
        ttab = {}

        for i in range(len(s)):
            if s[i] in stab:
                stab[s[i]] += 1
            else:
                stab[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] in ttab:
                ttab[t[i]] += 1
            else:
                ttab[t[i]] = 1

        if stab == ttab:
            return True
        
        return False