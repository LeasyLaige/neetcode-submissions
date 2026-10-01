class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subSet = set()
        left = 0
        subLength = 0

        for right in range(len(s)):
            while s[right] in subSet:
                subSet.remove(s[left])
                left += 1
            subSet.add(s[right])
            subLength = max(subLength, right - left + 1)


        return subLength