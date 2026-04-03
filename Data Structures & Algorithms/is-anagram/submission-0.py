class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ssorted = sorted(s)
        tsorted = sorted(t)
        if ssorted == tsorted:
            return True
        return False