class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = len(s)
        l1 = len(t)

        if l1 != l:
            return False

        return Counter(s) == Counter(t)
        