class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        firstString = {}
        secondString = {}

        for i in range(len(s)):
            firstString[s[i]] = (firstString.get(s[i]) or 0) + 1
            secondString[t[i]] = (secondString.get(t[i]) or 0) + 1

        return firstString == secondString
