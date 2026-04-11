class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        l1 = 0
        l2 = 0

        for i in range(min(len(word1), len(word2))):
            while l1 < len(word1) and l2 < len(word2):
                res += word1[l1]
                res += word2[l2]
                l1, l2 = l1+1, l2+1

            while l1 < len(word1):
                res += word1[l1]
                l1 += 1
            while l2 < len(word2):
                res += word2[l2]
                l2 += 1

        return res